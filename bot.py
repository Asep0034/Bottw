import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

TOKEN = os.environ.get("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim username Twitter/X siapa pun tanpa @")

async def track(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip().lstrip("@")
    url = f"https://memory.lol/tw/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200 and "No history found" not in response.text:
            await update.message.reply_text(f"📜 Riwayat username @{username}:\n{url}")
        else:
            await update.message.reply_text(f"Tidak ditemukan riwayat untuk @{username}")
    except Exception as e:
        await update.message.reply_text("Terjadi kesalahan saat memproses permintaan.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("track", track))
    app.add_handler(CommandHandler("", track))
    app.run_polling()
