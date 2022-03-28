# HoReCa | Job in EU 
# Was created by GAMch1k


# Imports
import telebot
from assets import settings
from assets.language_list import *
from assets.markups_list import *
from assets import database

bot = telebot.TeleBot(settings.TOKEN)   # Initializing bot

@bot.message_handler(commands=['start'])
def welcome(message):
    send = bot.send_message(message.chat.id, welcome_message, reply_markup=start_markup)
    bot.register_next_step_handler(send, choose_lang)


@bot.message_handler(content_types=['text'])
def choose_lang(message):
    send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
    bot.register_next_step_handler(send, choose_lang_check)


@bot.message_handler(content_types=['text'])
def choose_lang_check(message):
    if message.text == 'Українська':
        database.new_user(message.chat.id, 'ua')
    elif message.text == 'English':
        database.new_user(message.chat.id, 'en')
    elif message.text == 'Русский':
        database.new_user(message.chat.id, 'ru')

while True:
    try:
        bot.polling(none_stop=True, timeout=123)
    except:
        continue
