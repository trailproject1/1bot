from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Clear7 Bot is Online!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/auto on\n"
        "/auto off\n"
        "/time <minutes>\n"
        "/status\n"
        "/clean"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Clear7 Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
