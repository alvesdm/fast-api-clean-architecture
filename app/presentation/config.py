import os
from dotenv import load_dotenv

load_dotenv("app/presentation/.env")

class Config:
    API: str = "/api"
    API_V1_PREFIX: str = f"{API}/v1"
    API_V2_PREFIX: str = f"{API}/v2"
    SERVICE_NAME: str = os.getenv("SERVICE_NAME", "MyService")
    POSTS_DB_CNN: str = os.getenv("POSTS_DB_CNN")

configs = Config()