import logging

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

logger = logging.getLogger(__name__)


async def menu(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('Random Image')], [KeyboardButton('Random Person')]]
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='Welcome to my bot!',
                                   reply_markup=ReplyKeyboardMarkup(buttons))
