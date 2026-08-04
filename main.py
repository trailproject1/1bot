from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from database import init_db

from handlers.commands import start, help_command, status


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))

    print("✅ Clear7_bot Started Successfully")

    app.run_polling()


if __name__ == "__main__":
    main()
from telegram.ext import MessageHandler, filters
from handlers.messages import handle_message
app.add_handler(
    MessageHandler(filters.ALL, handle_message)
)
