from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config
import razorpay
from database import get_user
import threading
from webhook_handler import start_webhook

bot = Client("sub_bot", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)
client = razorpay.Client(auth=(config.RZP_KEY_ID, config.RZP_KEY_SECRET))

@bot.on_message(filters.command("start"))
async def start(client, message):
    user = get_user(message.from_user.id)
    status = "Active ✅" if user and user.status == "active" else "Inactive ❌"
    
    text = f"Welcome {message.from_user.first_name}!\n\nStatus: {status}\n\nNiche diye gaye buttons se subscription le sakte hain."
    buttons = [
        [InlineKeyboardButton("💳 Buy Subscription", callback_data="buy")],
        [InlineKeyboardButton("👤 My Account", callback_data="acc")]
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_callback_query(filters.regex("buy"))
async def buy_plans(client, callback):
    buttons = [
        [InlineKeyboardButton("Monthly Plan - ₹299", callback_data="plan_monthly")],
        [InlineKeyboardButton("Yearly Plan - ₹1999", callback_data="plan_yearly")]
    ]
    await callback.message.edit_text("Choose a plan:", reply_markup=InlineKeyboardMarkup(buttons))

# Admin Control Example
@bot.on_message(filters.command("stats") & filters.user(config.ADMIN_ID))
async def stats(client, message):
    await message.reply_text("Admin Dashboard: Coming Soon...")

if __name__ == "__main__":
    # Start Webhook in a separate thread
    threading.Thread(target=start_webhook, daemon=True).start()
    bot.run()
import os
import asyncio
from pyrogram import Client, filters
from flask import Flask
from threading import Thread

# --- Flask Server (Render Health Check ke liye) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Alive!"

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# --- Telegram Bot Logic ---
API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello! Bot is running perfectly on Render. ✅")

if __name__ == "__main__":
    # Flask ko alag thread mein chalayein
    Thread(target=run_flask).start()
    print("Starting Bot...")
    bot.run()
