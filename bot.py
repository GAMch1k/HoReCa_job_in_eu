# HoReCa | Job in EU 
# Was created by GAMch1k


# Imports
from operator import indexOf
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
        database.new_user(message.chat.id, 'ua')
        send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
        bot.register_next_step_handler(send, choose_lang_check)
    else:
        send = bot.send_message(message.chat.id, welcome_message, reply_markup=start_markup)
        bot.register_next_step_handler(send, choose_lang)


@bot.message_handler(content_types=['text'])
def choose_lang_check(message):
    if message.text == 'Українська':
        database.change_user_language(message.chat.id, 'ua')
        bot.send_message(message.chat.id, 'Встановлена Українська мова', reply_markup=empty)
    elif message.text == 'English':
        database.change_user_language(message.chat.id, 'en')
        bot.send_message(message.chat.id, 'Set to English language', reply_markup=empty)
    elif message.text == 'Русский':
        database.change_user_language(message.chat.id, 'ru')
        bot.send_message(message.chat.id, 'Установлен Русский язык', reply_markup=empty)
    else:
        send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
        bot.register_next_step_handler(send, choose_lang_check)
    # print(message)
    bot.send_message(message.chat.id, what_need_to_do[0], reply_markup=get_countrees_markup(database.get_user_lang(message.chat.id)))
    # bot.register_next_step_handler(send, choose_country)


@bot.message_handler(content_types=['text'])
def choose_country(message):
    # if(message.text != ''):
    database.update_post_value(message.chat.id, 'city', message.text)
    database.print_all_posts()
    send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
    bot.register_next_step_handler(send, choose_lang_check)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data:
        database.new_post(call.from_user.id, call.data)
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text=f'You choosed {countrees_list[callbacks_list.index(call.data)][check_lang(database.get_user_lang(call.from_user.id))]}')
        send = bot.send_message(call.from_user.id, choose_city[check_lang(database.get_user_lang(call.from_user.id))])
        bot.register_next_step_handler(send, choose_country)

# Infinity loop fixing crush
# while True:
#     try:
#         bot.polling(none_stop=True, timeout=123)
#     except:
#         continue

bot.polling(none_stop=True, timeout=123)
