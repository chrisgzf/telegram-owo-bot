import logging
import telegram
import sys
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters)

# Setting up the logger
logging.basicConfig(level=logging.DEBUG,
                    format=('%(asctime)s - %(name)s - %(levelname)s'
                            ' - %(message)s'))
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Obtaining the bot secrets
try:
    import bot_secrets
except:
    logger.critical("No bot token found. Please set up bot_secrets.py"
                    " properly. Read the README on how to set it up.")
    sys.exit(1)

BOT_TOKEN = bot_secrets.TOKEN

# Setting up the bot
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Long pre-defined messages go here
START_MESSAGE = ("Welcome to the OwO Bot!\n\n"
                 "This bot was created to help you owoify text.\n"
                 "If you would like to contribute to the development "
                 "of this bot, please visit "
                 "https://github.com/chrisgzf/telegram-owo-bot.")

# Handling functions go here
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=START_MESSAGE)

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=update.message.text)

# Handlers go here
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

# Start polling the bot
updater.start_polling()
