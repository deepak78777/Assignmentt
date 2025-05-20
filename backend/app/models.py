from pydantic import BaseModel, EmailStr
from typing import List

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    id: int
    email: str

class UserProfile(BaseModel):
    email: EmailStr
    name: str
    location: str
    years_experience: int
    skills: List[str]
    job_type: str  # remote / onsite / any