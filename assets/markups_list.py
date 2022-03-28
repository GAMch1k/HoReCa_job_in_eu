# 0 - ua
# 1 - en
# 2 - ru

from telebot import types


start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_btn = types.KeyboardButton('Старт / Start')
start_markup.add(start_btn)


choose_lang_marukp = types.ReplyKeyboardMarkup(resize_keyboard=True)
ua_btn = types.KeyboardButton('Українська')
en_btn = types.KeyboardButton('English')
ru_btn = types.KeyboardButton('Русский')
choose_lang_marukp.add(ua_btn, en_btn, ru_btn)
