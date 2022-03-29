# 0 - ua
# 1 - en
# 2 - ru


# Imports
from telebot import types
from assets.language_list import *


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
                countrees_list[i][lang], callback_data=callbacks_list[i]
            ),
            types.InlineKeyboardButton(text=
                countrees_list[i+1][lang], callback_data=callbacks_list[i+1]
            )
        )
    return countrees_markup
