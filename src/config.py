import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(".env.local")

class Settings(BaseSettings):
    PROJECT_NAME: str = "Fruit Shop API"
    
    # Environment variables loaded from .env.local
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "pg.krishb.in")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")

    @property
    def get_db_url(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env.local"
        extra = "allow"

settings = Settings()
