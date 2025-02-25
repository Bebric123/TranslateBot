import os
from flask import Flask
from deep_translator import GoogleTranslator
from lingua import Language, LanguageDetectorBuilder
import config
import telebot
import threading

bot = telebot.TeleBot(config.token)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

languages = [Language.ENGLISH, Language.RUSSIAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

@bot.message_handler(func=lambda m: True)
def trans(message):
    if detector.detect_language_of(message.text)==Language.ENGLISH:
        translated_text = GoogleTranslator(source='en', target='ru').translate(message.text)
    else:
        translated_text = GoogleTranslator(source='ru', target='en').translate(message.text)
    bot.send_message(message.chat.id,translated_text)
def run():
    app.run(host='0.0.0.0', port=8080)
threading.Thread(target=run).start()
bot.polling()