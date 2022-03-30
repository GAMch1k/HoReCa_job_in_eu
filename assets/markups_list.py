# 0 - ua
# 1 - en
# 2 - ru


# Imports
from telebot import types
from assets.language_list import *


empty = types.ReplyKeyboardRemove()


start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = types.KeyboardButton('Старт / Start')
start_markup.add(start_btn)


choose_lang_marukp = types.ReplyKeyboardMarkup(resize_keyboard=True)
ua_btn = types.KeyboardButton('Українська')
en_btn = types.KeyboardButton('English')
ru_btn = types.KeyboardButton('Русский')
choose_lang_marukp.add(ua_btn, en_btn, ru_btn)

def get_countrees_markup(lang):
    lang = check_lang(lang)

    countrees_markup = types.InlineKeyboardMarkup()
    for i in range(0, len(countrees_list)-1, 2):
        countrees_markup.row(
            types.InlineKeyboardButton(text=
                f'{countrees_flags[i]} {countrees_list[i][lang]}', callback_data=callbacks_list[i]
            ),
            types.InlineKeyboardButton(text=
                f'{countrees_flags[i+1]} {countrees_list[i+1][lang]}', callback_data=callbacks_list[i+1]
            )
        )
    return countrees_markup


def get_editing_markup(lang):
    lang = check_lang(lang)

    edit_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    edit_markup.row(
        types.KeyboardButton(edit_info_company[lang])
    )
    edit_markup.row(
        types.KeyboardButton(edit_vacation[lang]),
        types.KeyboardButton(edit_duties[lang])
    )
    edit_markup.row(
        types.KeyboardButton(edit_requirments[lang]),
        types.KeyboardButton(edit_conditions[lang])
    )
    edit_markup.row(
        types.KeyboardButton(edit_photo_logo[lang]),
        types.KeyboardButton(edit_contacts[lang])
    )
    edit_markup.row(
        types.KeyboardButton(edit_empty_vacation[lang])
    )
    edit_markup.row(
        types.KeyboardButton(edit_accept[lang])
    )
    return edit_markup


def get_main_menu_markup(lang):
    lang = check_lang(lang)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton(menu_create_vacation[lang]))
    markup.row(types.KeyboardButton(manu_share_chanel[lang]))
    markup.row(types.KeyboardButton(menu_support[lang]))
    
    return markup


def generate_accept(post_id):
    accept = types.InlineKeyboardMarkup()
    accept.row(types.InlineKeyboardButton(text='✅ Одобрить', callback_data=f'{post_id}'))
    return accept
