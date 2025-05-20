from fastapi import FastAPI, HTTPException
from app.models import UserCreate, UserLogin, UserProfile
from app.auth import get_password_hash, verify_password, create_access_token
from app.database import users_collection, profiles_collection

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # your frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/signup")
def signup(user: UserCreate):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed = get_password_hash(user.password)
    users_collection.insert_one({"email": user.email, "password": hashed})
    return {"message": "User registered"}

@app.post("/login")
def login(user: UserLogin):
    db_user = users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/profile")
def save_profile(profile: UserProfile):
    existing = profiles_collection.find_one({"email": profile.email})
    if existing:
        profiles_collection.replace_one({"email": profile.email}, profile.dict())
    else:
        profiles_collection.insert_one(profile.dict())
    return {"message": "Profile saved"}