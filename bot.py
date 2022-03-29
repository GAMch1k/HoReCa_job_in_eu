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
    if message.text == 'Старт / Start':
        send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
        bot.register_next_step_handler(send, choose_lang_check)
    else:
        send = bot.send_message(message.chat.id, welcome_message, reply_markup=start_markup)
        bot.register_next_step_handler(send, choose_lang)


@bot.message_handler(content_types=['text'])
def choose_lang_check(message):
    database.new_user(message.chat.id, 'en')
    if message.text == 'Українська':
        database.change_user_language(message.chat.id, 'ua')
        bot.send_message(message.chat.id, 'Встановлена Українська мова')
    elif message.text == 'English':
        database.change_user_language(message.chat.id, 'en')
        bot.send_message(message.chat.id, 'Set to English language')
    elif message.text == 'Русский':
        database.change_user_language(message.chat.id, 'ru')
        bot.send_message(message.chat.id, 'Установлен Русский язык')
    else:
        send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
        bot.register_next_step_handler(send, choose_lang_check)

    send = bot.send_message(message.chat.id, what_need_to_do[0], reply_markup=get_countrees_markup(database.get_user_lang(message.chat.id)))
    bot.register_next_step_handler(send, choose_country)


@bot.message_handler(content_types=['text'])
def choose_country(message):
    pass


# @bot.callback_query_handler(func=lambda call: True)
# def callback_query(call):
#     if call.data == "cb_yes":
#         bot.answer_callback_query(call.id, "Answer is Yes")

# Infinity loop fixing crush
# while True:
#     try:
#         bot.polling(none_stop=True, timeout=123)
#     except:
#         continue

bot.polling(none_stop=True, timeout=123)
