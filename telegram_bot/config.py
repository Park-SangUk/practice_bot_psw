import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "1412239527:AAF1pdPEj61ea51kC0HT01unsodh97HKLok")
CHAT_ID = os.environ.get("CHAT_ID", "practice_bot_psw")

if not TELEGRAM_TOKEN or not CHAT_ID:
    raise Exception("TELEGRAM_TOKEN, CHAT_ID 확인필요")