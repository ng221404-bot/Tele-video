import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from .config import *

async def animate_message(update: Update, context: ContextTypes.DEFAULT_TYPE, messages: list, duration: float = 0.5):
    """Edits a message sequentially to create an animation effect."""
    message = None
    if update.callback_query:
        message = update.callback_query.message
    elif update.message:
        message = update.message
        
    if not message:
        return

    for msg in messages:
        try:
            await message.edit_text(msg, parse_mode='Markdown')
            await asyncio.sleep(duration)
        except Exception:
            # Handle cases where message content is same or message deleted
            pass

async def send_to_admin(context: ContextTypes.DEFAULT_TYPE, text: str, reply_markup=None):
    """Sends a message to the admin chat."""
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
