from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN
from database import init_db


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Clear7_bot is Online!"
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
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Database Loaded")
    print("✅ Clear7_bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
