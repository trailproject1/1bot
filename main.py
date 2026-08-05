from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)
from config import BOT_TOKEN
from database import init_db

from handlers.commands import (
    start,
    help_command,
    status,
    auto_on,
    auto_off,
    time,
)
from handlers.messages import handle_message

def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("auto_on", auto_on))
    app.add_handler(CommandHandler("auto_off", auto_off))
    app.add_handler(CommandHandler("time", time))
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("✅ Clear7_bot Started Successfully")

    app.run_polling()


if __name__ == "__main__":
    main()
