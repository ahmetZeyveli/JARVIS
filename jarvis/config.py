import os
from pathlib import Path
from pydantic_settings import BaseSettings

# Projenin kök dizinini otomatik bulur (C:\Users\asus\Downloads\JARVIS)
ROOT_DIRECTORY = Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    chat_model: str = "deepseek-chat"

    class Config:
        env_file = ROOT_DIRECTORY / ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()