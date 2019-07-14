import logging
import sys
from telegram import (InlineQueryResultArticle, InputTextMessageContent, ParseMode)
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
START_MESSAGE = ("_UwU_... Nice to meet you {}-sama!\n\n"
                 "I am here to help you owoify text!\n\n"
                 "*Functions:*\n"
                 "1. Inline query: In any conversation (group or "
                 "individual), just type `@OwoifyBot` and I can owoify text "
                 "anywhere (even groups I'm not in)!\n"
                 "2. Just PM me and I can owoify whatever you "
                 "say!\n"
                 "3. Group messages: reply to any group message with `/owo`\n\n"
                 "To contribute to the development "
                 "of this bot, please [click here]"
                 "(https://github.com/chrisgzf/telegram-owo-bot).")


# Handling functions go here
def start(update, context):
    userid = update.message.from_user["id"]
    try:
        username = update.message.from_user["username"]
    except:
        username = userid
    firstname = update.message.from_user["first_name"]
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=START_MESSAGE.format(firstname),
                             disable_web_page_preview=True,
                             parse_mode=ParseMode.MARKDOWN)
    logger.info(f"{username} {userid}: /start")


def echo(update, context):
    userid = update.message.chat_id
    try:
        username = update.message.from_user["username"]
    except:
        username = userid
    text = update.message.text
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=owoify(text),
                             disable_web_page_preview=True)
    logger.info(f"{username} {userid}: {text}")


def owo(update, context):
    userid = update.message.chat_id
    try:
        username = update.message.from_user["username"]
    except:
        username = userid
    try:
        text = update.message.reply_to_message.text
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=("Bbb..but master-sama, you need to reply to a message! "
                                      "I have no idea what text you want to be owoified..."
                                      " (｡•́︿•̀｡)"))
        return
    context.bot.send_message(chat_id=update.message.chat_id,
                             text=owoify(text),
                             reply_to_message_id=update.message.reply_to_message.message_id,
                             disable_web_page_preview=True)
    logger.info(f"{username} {userid} GROUP: {text}")


# Handlers go here
start_handler = CommandHandler('start', start)
owo_handler = CommandHandler('owo', owo)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(owo_handler)
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
            title='Owoified Text Preview (press to send)',
            description=owoify(query),
            thumb_url='https://avatarfiles.alphacoders.com/161/161188.png',
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
