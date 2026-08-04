from telegram.ext import Application, CommandHandler
from config import BOT_TOKEN
from database import init_db

from handlers.commands import start, help_command


def main():
    init_db()

    app = Application.builder().token(BOT_TOKEN).build()

    from handlers.commands import start, help_command
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Clear7_bot Started Successfully")

    app.run_polling()


if __name__ == "__main__":
    main()
