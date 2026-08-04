# Delete scheduler
import asyncio
from telegram.error import TelegramError


async def delete_message(context):
    job = context.job

    chat_id = job.data["chat_id"]
    message_id = job.data["message_id"]

    try:
        await context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

    except TelegramError as e:
        print(f"Delete failed: {e}")


def schedule_delete(job_queue, chat_id, message_id, minutes):
    job_queue.run_once(
        delete_message,
        when=minutes * 60,
        data={
            "chat_id": chat_id,
            "message_id": message_id
        },
        name=f"{chat_id}_{message_id}"
    )
