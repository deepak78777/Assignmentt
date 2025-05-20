# database.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)

db = client["jobmatch"]
users_collection = db["users"]
profiles_collection = db["profiles"]
jobs_collection = db["jobs"]
