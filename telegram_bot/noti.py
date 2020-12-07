from config import TELEGRAM_TOKEN, CHAT_ID
import requests
import telegram

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send(msg):
    bot.sendMessage(CHAT_ID, msg, parse_mode=telegram.ParseMode.HTML)