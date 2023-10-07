"""Entry point for the application."""
import logging

from dotenv import load_dotenv
from telegram import Update, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

from requests import *

import commands
from db.connection import DBHandler

randomPeopleText = 'Random Person'
randomPeopleUri = 'https://thispersondoesnotexist.com/'
randomImageText = 'Random Image'
randomImageUri = 'https://picsum.photos/200/300'

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Do this on every module that you want to use
logger = logging.getLogger(__name__)


# Logs telegram api errors
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


async def messageHandler(update: Update, context: CallbackContext):
    if randomPeopleText in update.message.text:
        image = get(randomPeopleUri).content
    if randomImageText in update.message.text:
        image = get(randomImageUri).content

    await context.bot.sendMediaGroup(chat_id=update.effective_chat.id, media=[InputMediaPhoto(image, caption='')])
    buttons = [[InlineKeyboardButton('👍🏻', callback_data='like')],
               [InlineKeyboardButton('👎🏻', callback_data='dislike')]]
    await context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                                   text='Te gusto la imagen?')


def main():
    """Start the bot."""

    app = ApplicationBuilder().token("5820768310:AAH5idM3TIfen4fkKsL41mZjDmT5Pr8Jolg").build()  # os.getenv("TOKEN")

    DBHandler().connect_pool()

    app.add_error_handler(error)

    app.add_handlers(
        [
            CommandHandler(command, getattr(commands, command))
            for command in commands.get_all_commands()
        ]
    )

    app.add_handler(MessageHandler(filters.COMMAND, commands.unknown))
    app.add_handler(MessageHandler(filters.TEXT, messageHandler))
    app.run_polling()


if __name__ == "__main__":
    main()
