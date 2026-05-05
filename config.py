import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 29270492))
API_HASH = os.getenv("API_HASH", "c0ff4a728d5da8de25807766b2901111")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8674402252:AAGlHWN0pFWlX1vIwFhdXuUnE3akYiys4ik")
ADMIN_ID = int(os.getenv("ADMIN_ID", 7990200132))

# Razorpay Config
RZP_KEY_ID = os.getenv("RZP_KEY_ID", "")
RZP_KEY_SECRET = os.getenv("RZP_KEY_SECRET", "")
RZP_WEBHOOK_SECRET = os.getenv("RZP_WEBHOOK_SECRET", "")

# Channel Details
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))
DB_URL = os.getenv("DATABASE_URL", "sqlite:///bot.db")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "") # Render URL
