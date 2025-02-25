from deep_translator import GoogleTranslator
from lingua import Language, LanguageDetectorBuilder
import config
import telebot
from langdetect import detect

bot = telebot.TeleBot(config.token)
languages = [Language.ENGLISH, Language.RUSSIAN]
detector = LanguageDetectorBuilder.from_languages(*languages).build()

@bot.message_handler(func=lambda m: True)
def trans(message):
    if detector.detect_language_of(message.text)==Language.ENGLISH:
        translated_text = GoogleTranslator(source='en', target='ru').translate(message.text)
    else:
        translated_text = GoogleTranslator(source='ru', target='en').translate(message.text)
    bot.send_message(message.chat.id,translated_text)
bot.polling()