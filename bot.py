# HoReCa | Job in EU 
# Was created by GAMch1k


# Imports
from operator import indexOf
import telebot
from assets import settings
from assets.functions import get_full_post
from assets.language_list import *
from assets.markups_list import *
from assets import database
import cv2


bot = telebot.TeleBot(settings.TOKEN)   # Initializing bot


@bot.message_handler(commands=['start'])
def welcome(message):
    send = bot.send_message(message.chat.id, welcome_message, reply_markup=start_markup)
    bot.register_next_step_handler(send, choose_lang)


@bot.message_handler(content_types=['text'])
def choose_lang(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if message.text == 'Старт / Start':
        database.new_user(message.chat.id, 'ua')
        send = bot.send_message(message.chat.id, choose_language, reply_markup=choose_lang_marukp)
        bot.register_next_step_handler(send, choose_lang_check)
    else:
        send = bot.send_message(message.chat.id, welcome_message, reply_markup=start_markup)
        bot.register_next_step_handler(send, choose_lang)


@bot.message_handler(content_types=['text'])
def choose_lang_check(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
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

    bot.send_message(message.chat.id, what_need_to_do[0], reply_markup=get_countrees_markup(database.get_user_lang(message.chat.id)))
    # bot.register_next_step_handler(send, set_city)
    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data:
        database.new_post(call.from_user.id, call.data)
        bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text=f'You choosed {countrees_list[callbacks_list.index(call.data)][check_lang(database.get_user_lang(call.from_user.id))]}')
        send = bot.send_message(call.from_user.id, choose_city[check_lang(database.get_user_lang(call.from_user.id))])
        bot.register_next_step_handler(send, set_city)


@bot.message_handler(content_types=['text'])
def set_city(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'city', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, set_institytion_type_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_institytion_type)


@bot.message_handler(content_types=['text'])
def set_institytion_type(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'institution_type', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, set_institytion_name_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_institytion_name)


@bot.message_handler(content_types=['text'])
def set_institytion_name(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'institution_name', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, vacation_name[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_vacation_name)


@bot.message_handler(content_types=['text'])
def set_vacation_name(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'job_name', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, duties_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_duties)


@bot.message_handler(content_types=['text'])
def set_duties(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'duties', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, requirements_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_requirements)


@bot.message_handler(content_types=['text'])
def set_requirements(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'requirements', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, job_conditions_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_job_conditions)


@bot.message_handler(content_types=['text'])
def set_job_conditions(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'job_conditions', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, contact_info_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_contact_info)


@bot.message_handler(content_types=['text'])
def set_contact_info(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'contact_info', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, download_photo)


@bot.message_handler(content_types=['photo'])
def download_photo(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    try:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        img_id = database.get_post_id(message.chat.id)
        with open(f'assets/images/{img_id}.jpg', 'wb') as f:
            f.write(downloaded_file)
        height, width, c = cv2.imread(f'assets/images/{img_id}.jpg').shape
        if width >= height:
            bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))])
            
            send = bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id)}',
                parse_mode='html')

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, download_photo)

    except:
        send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
        bot.register_next_step_handler(send, download_photo)


@bot.message_handler(content_types=['text'])
def editing_post(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'contact_info', message.text)
        if database.is_post_editing(message.chat.id):
            print('EDITING POST!')
        else:
            send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, download_photo)


# Infinity loop which can fix crush
# while True:
#     try:
#         bot.polling(none_stop=True, timeout=123)
#     except:
#         continue

bot.infinity_polling()
