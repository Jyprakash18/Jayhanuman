import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# Razorpay Config
RZP_KEY_ID = os.getenv("RZP_KEY_ID", "")
RZP_KEY_SECRET = os.getenv("RZP_KEY_SECRET", "")
RZP_WEBHOOK_SECRET = os.getenv("RZP_WEBHOOK_SECRET", "")

# Channel Details
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
DB_URL = os.getenv("DATABASE_URL", "sqlite:///bot.db")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "") # Render URL
