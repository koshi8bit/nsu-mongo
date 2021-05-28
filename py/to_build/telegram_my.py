import telegram


class TelegramMy:
    def __init__(self, bot_token, chat_id):
        self.bot = telegram.Bot(token=bot_token)
        self.chat_id = chat_id

    def send(self, text):
        self.bot.sendMessage(chat_id=self.chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
