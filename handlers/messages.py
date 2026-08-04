from telegram import Update
from telegram.ext import ContextTypes

from database import get_settings
from scheduler.delete_scheduler import schedule_delete


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message is None:
        return

    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    auto_delete, delete_time = get_settings(chat_id)

    if auto_delete:
        schedule_delete(
            context.job_queue,
            chat_id,
            message_id,
            delete_time
        )
