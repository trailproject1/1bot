from telegram import Update
from telegram.ext import ContextTypes

from database import (
    get_settings,
    set_auto,
    set_time
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Clear7_bot is Online!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start\n"
        "/help\n"
        "/status\n"
        "/auto_on\n"
        "/auto_off\n"
        "/time <minutes>"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    auto_delete, delete_time = get_settings(
        update.effective_chat.id
    )

    status_text = "ON" if auto_delete else "OFF"

    await update.message.reply_text(
        f"Auto Delete : {status_text}\n"
        f"Timer : {delete_time} Minutes"
    )


async def auto_on(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_auto(update.effective_chat.id, 1)

    await update.message.reply_text(
        "✅ Auto Delete Enabled"
    )


async def auto_off(update: Update, context: ContextTypes.DEFAULT_TYPE):
    set_auto(update.effective_chat.id, 0)

    await update.message.reply_text(
        "❌ Auto Delete Disabled"
    )


async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text(
            "Usage: /time 10"
        )
        return

    minutes = int(context.args[0])

    set_time(
        update.effective_chat.id,
        minutes
    )

    await update.message.reply_text(
        f"⏱ Timer updated to {minutes} minutes."
    )
