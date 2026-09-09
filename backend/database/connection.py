import os 
import certifi
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(
    MONGODB_URL,
    tls = True,
    tlsCAfile=certifi.where(),
    serverSelectionTimeoutMS=3000,
    )

db = client[DATABASE_NAME] 

try:
    client.admin.command("ping")
    print("MongoDB connection successful!")
except Exception as e:
    print("MongoDB connection failed:")
    print(e)