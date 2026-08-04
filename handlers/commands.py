from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Clear7_bot is online!\n\n"
        "Use /help to view available commands."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Available Commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help\n"
        "/status - Show bot status\n"
        "/auto on - Enable auto delete\n"
        "/auto off - Disable auto delete\n"
        "/time 10 - Set delete timer\n"
        "/clean - Clean messages"
    )
