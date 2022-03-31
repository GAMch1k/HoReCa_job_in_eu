# HoReCa | Job in EU 
# Was created by GAMch1k


# Imports
import telebot
from assets import settings
from assets.functions import get_full_post
from assets.language_list import *
from assets.markups_list import *
from assets import database
import cv2
import os


bot = telebot.TeleBot(settings.TOKEN)   # Initializing bot

MODERATORS_CHANEL = '@tests_for_my_bots_dont_matter'    # Chanel where moderators redacting posts
FORWARD_TO = -1001279412171


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

    bot.send_message(message.chat.id, what_need_to_do[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_countrees_markup(database.get_user_lang(message.chat.id)))
    # bot.register_next_step_handler(send, set_city)
    

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        id = int(call.data)
        bot.send_message(
            database.get_user_id_by_post_id(id),
            post_confirmed_message[check_lang(database.get_user_lang(call.from_user.id))])
        
        msg_id = database.get_post_data(0, 'mods_chat_id', id)
        # bot.forward_message(FORWARD_TO, MODERATORS_CHANEL, msg_id)
        bot.copy_message(FORWARD_TO, MODERATORS_CHANEL, msg_id, parse_mode='html')
        bot.delete_message(MODERATORS_CHANEL, msg_id)
        bot.answer_callback_query(call.id, "✅ Одобрено")
    except Exception as e:
        print(e)

        if call.data:
            database.new_post(call.from_user.id, call.data)
            bot.edit_message_text(chat_id=call.from_user.id, message_id=call.message.id, text=f'{you_choosed[check_lang(database.get_user_lang(call.from_user.id))]} {countrees_flags[callbacks_list.index(call.data)]} {countrees_list[callbacks_list.index(call.data)][check_lang(database.get_user_lang(call.from_user.id))]}')
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
            send = bot.send_message(message.chat.id, set_institytion_name_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_institytion_name)
        else:
            send = bot.send_message(message.chat.id, set_institytion_name_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_institytion_name)


@bot.message_handler(content_types=['text'])
def set_institytion_name(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'institution_name', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, vacation_name[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_vacation_name)


@bot.message_handler(content_types=['text'])
def set_vacation_name(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'job_name', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, duties_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_duties)


@bot.message_handler(content_types=['text'])
def set_duties(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'duties', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, requirements_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_requirements)


@bot.message_handler(content_types=['text'])
def set_requirements(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'requirements', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, job_conditions_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_job_conditions)


@bot.message_handler(content_types=['text'])
def set_job_conditions(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'job_conditions', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, contact_info_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, set_contact_info)


@bot.message_handler(content_types=['text'])
def set_contact_info(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        database.update_post_value(message.chat.id, 'contact_info', message.text)
        database.update_user_value(message.chat.id, 'contact_info', message.text)
        if database.is_post_editing(message.chat.id):
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
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
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
            
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            database.update_post_value(message.chat.id, 'editing', True)
            bot.register_next_step_handler(send, editing_post)
        else:
            send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
            bot.register_next_step_handler(send, download_photo)

    except Exception as e:
        print(e)
        send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))])
        bot.register_next_step_handler(send, download_photo)


@bot.message_handler(content_types=['text'])
def editing_post(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        _not_found = True
        for i in edit_info_company:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, set_institytion_type_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_institytion_type)
        for i in edit_vacation:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, vacation_name[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_vacation_name)
        for i in edit_duties:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, duties_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_duties)
        for i in edit_requirments:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, requirements_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_requirements)
        for i in edit_conditions:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, job_conditions_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_job_conditions)
        for i in edit_photo_logo:
            if message.text == i and _not_found:
                _not_found = False
                send = bot.send_message(message.chat.id, send_photo_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, download_photo)
        for i in edit_contacts:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, contact_info_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.register_next_step_handler(send, set_contact_info)
        for i in edit_empty_vacation:
            if message.text == i:
                _not_found = False
                
                img_id = database.get_post_id(message.chat.id)
                os.remove(f'assets/images/{img_id}.jpg')
                database.delete_last_users_post(message.chat.id)
                send = bot.send_message(message.chat.id, clearing_all_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_main_menu_markup(database.get_user_lang(message.chat.id), database.is_user_admin(message.chat.id)))
                bot.register_next_step_handler(send, main_menu)
        for i in edit_accept:
            if message.text == i:
                _not_found = False
                img_id = database.get_post_id(message.chat.id)
                mod = bot.send_photo(MODERATORS_CHANEL,
                    photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                    caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                    parse_mode='html',
                    reply_markup=generate_accept(img_id))
                database.update_post_value(message.chat.id, 'mods_chat_id', mod.message_id)
                send = bot.send_message(message.chat.id, send_to_the_moderators_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_main_menu_markup(database.get_user_lang(message.chat.id), database.is_user_admin(message.chat.id)))
                bot.register_next_step_handler(send, main_menu)
        
        if _not_found:
            img_id = database.get_post_id(message.chat.id)
            bot.send_photo(message.chat.id,
                photo=open(f'assets/images/{img_id}.jpg', 'rb'),
                caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
                parse_mode='html')
        
            send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

            bot.register_next_step_handler(send, editing_post)

    else:
        img_id = database.get_post_id(message.chat.id)
        bot.send_photo(message.chat.id,
            photo=open(f'assets/images/{img_id}.jpg', 'rb'),
            caption=f'{get_full_post(message.chat.id, check_lang(database.get_user_lang(message.chat.id)))}',
            parse_mode='html')
        
        send = bot.send_message(message.chat.id, edit_label_lang[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_editing_markup(database.get_user_lang(message.chat.id)))

        bot.register_next_step_handler(send, editing_post)


@bot.message_handler(content_types=['text'])
def main_menu(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    if(message.text != ''):
        _not_found = True
        for i in menu_create_vacation:
            if message.text == i:
                _not_found = False
                bot.send_message(message.chat.id, starting_new_vacation[check_lang(database.get_user_lang(message.chat.id))], reply_markup=empty)
                bot.send_message(message.chat.id, what_need_to_do[check_lang(database.get_user_lang(message.chat.id))], reply_markup=get_countrees_markup(database.get_user_lang(message.chat.id)))
        for i in manu_share_chanel:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, share_chanel_lang[check_lang(database.get_user_lang(message.chat.id))])
                bot.register_next_step_handler(send, main_menu)
        for i in menu_support:
            if message.text == i:
                _not_found = False
                send = bot.send_message(message.chat.id, tech_support_lang[check_lang(database.get_user_lang(message.chat.id))])
                bot.register_next_step_handler(send, main_menu)
        for i in admin_damp:
            if message.text == i and _not_found:
                _not_found = False
                database.dump_to_excel()
                f = open('assets/database/excel_db.xlsx', 'rb')
                send = bot.send_document(message.chat.id, f)
                bot.register_next_step_handler(send, main_menu)
        for i in admin_mail:
            if message.text == i:
                _not_found = False
        if _not_found:
            pass


# Infinity loop which can fix crush
# while True:
#     try:
#         bot.polling(none_stop=True, timeout=123)
#     except:
#         continue

bot.infinity_polling()
