from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

class Settings:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
    CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "300"))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///rentbot.db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
