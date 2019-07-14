import logging
import sys
from telegram import (InlineQueryResultArticle, InputTextMessageContent)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          InlineQueryHandler, Filters)
from owoify import owoify

# Setting up the logger
logging.basicConfig(level=logging.DEBUG,
                    format=('%(asctime)s %(levelname)s: %(message)s'))
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
    userid = update.message.from_user["id"]
    try:
        username = update.message.from_user["username"]
    except:
        username = userid
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=START_MESSAGE)
    logger.info(f"{username} {userid}: /start")


def echo(update, context):
    userid = update.message.chat_id
    try:
        username = update.message.from_user["username"]
    except:
        username = userid
    text = update.message.text
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=owoify(text))
    logger.info(f"{username} {userid}: {text}")


# Handlers go here
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)


# Setting up inline queries
def inline_owoify(update, context):
    query = update.inline_query.query
    if not query:
        return
    userid = update.effective_user.id
    username = update.effective_user.username
    logger.info(f"{username} {userid} INLINE: {query}")
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=0,
            title='Owoified Text',
            input_message_content=InputTextMessageContent(owoify(query))
        )
    )
    context.bot.answer_inline_query(update.inline_query.id,
                                    results,
                                    cache_time=0)


inline_owoify_handler = InlineQueryHandler(inline_owoify)
dispatcher.add_handler(inline_owoify_handler)

# Start polling the bot
updater.start_polling()
