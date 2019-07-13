# OwO Bot

This is a bot that OwOifies text. So what exactly is OwOified text then you might ask?

This is OwOified text:
```
Fow exampwe, this is what a OwOified text wooks wike! >w< It sounds wike Engwish yet has some hints of.... kawaiinyess?
```

# Installing

1. Clone the repo including the python-telegram-bot folder with

```
$ git clone https://github.com/chrisgzf/telegram-owo-bot --recursive
```

2. In your preferred virtualenv / conda env, install the `python-telegram-bot` library with

```
$ cd telegram-owo-bot/python-telegram-bot`
$ python setup.py install
```

3. Obtain your bot token by talking to @BotFather on Telegram, then follow the instructions in `bot_secrets_SAMPLE.py` to properly add your bot token.

4. Run the bot by running `python owo_main_bot.py`

# Development Roadmap

- Support for groups will be added soon
- Better OwOification of text will be researched
- Support for gradual increasing OwOification of a body of text is planned to be explored
- Sentiment analysis of a body of text, and appending it with respective kaomojis that reflect the tone of the text will be explored as well, to make this a truly "AI-powered OwOification engine"

# Privacy

This bot WILL NOT record nor save your messages. I do my testing entirely on my own, with my own messages that I type and send my own bot. You can check the source code to see that I indeed do not save your messages and usage information.

I do however, plan on coding a feature that will record how many users have used the bot. This has not been implemented yet.

# Contribution to the Project

Just submit a PR. Document and code well.

