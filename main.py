import os
import asyncio
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Dummy web server for Render Web Service Free Tier
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is alive and running!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app_web.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# Auto delete delay: 10 minutes (600 seconds)
DELETE_DELAY = 600

async def delete_message_after_delay(context: ContextTypes.DEFAULT_TYPE):
    """Job callback to delete a message after timer expires."""
    job_data = context.job.data
    chat_id = job_data["chat_id"]
    message_id = job_data["message_id"]
    
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except Exception as e:
        print(f"Failed to delete message {message_id} in {chat_id}: {e}")

async def auto_clean_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Monitors messages and schedules them for deletion after 10 minutes."""
    if not update.effective_message or not update.effective_chat:
        return
        
    chat_id = update.effective_chat.id
    message_id = update.effective_message.message_id

    # Schedule deletion task using JobQueue
    context.job_queue.run_once(
        delete_message_after_delay,
        when=DELETE_DELAY,
        data={"chat_id": chat_id, "message_id": message_id},
    )

async def purge_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manual Purge: Deletes up to 100 recent messages instantly (Admin only)."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # Check if user is an admin
    member = await context.bot.get_chat_member(chat_id, user_id)
    if member.status not in ["administrator", "creator"]:
        await update.message.reply_text("⚠️ Only admins can use /purge.")
        return

    current_msg_id = update.message.message_id
    deleted_count = 0

    # Loop through previous message IDs to bulk delete
    for msg_id in range(current_msg_id, max(1, current_msg_id - 100), -1):
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            deleted_count += 1
        except Exception:
            continue

    status_msg = await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🧹 Purged {deleted_count} messages."
    )
    
    # Auto-delete the confirmation message after 5 seconds
    await asyncio.sleep(5)
    try:
        await status_msg.delete()
    except Exception:
        pass

def main():
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable not set!")

    # Start dummy web server for Render keep-alive
    keep_alive()

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Admin Purge Command (/purge)
    app.add_handler(CommandHandler("purge", purge_command))

    # Admin Purge Command (/purge)
    app.add_handler(CommandHandler("purge", purge_command))

    # Auto Clean Handler (ALL messages including Bot replies and service updates)
    # Note: ~filters.COMMAND-a remove pannirukom, and filters.ALL paka-va work aagum!
    app.add_handler(
        MessageHandler(
            filters.ALL, 
            auto_clean_handler
        )
    )

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
