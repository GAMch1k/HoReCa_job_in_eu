# 0 - ua
# 1 - en
# 2 - ru


def check_lang(lang):
    if (lang == 'ua'): return 0
    if (lang == 'en'): return 1
    return 2


# welcome_message = '''
# HoReCa | Job in EU – створено для допомоги людям із України.
# Тут ви можете надати роботу для українців в інших країнах.

# HoReCa | Job in EU – создан для помощи людям из Украины.
# Здесь вы можете предоставить работы для украинцев в других странах.

# HoReCa | Work in the EU – created for help people from Ukraine.
# You can provide jobs for Ukrainians in other European countries and beyond.
# '''

choose_language = '''
Оберіть будь ласка мову бота
для зручної комунікації.

Выберите пожалуйста язык
бота для удобной коммуникации.

Select please the bot language
for easy communication.
'''

create_vacation_butt = [
    '📝 Створити вакансію',
    '📝 Create vacation',
    '📝 Создать вакансию'
]

starting_creating_vacation = [
    'Створюємо нову вакансію',
    'Creating new vacation',
    'Создаем новую вакансию'
]

starting_new_vacation = [
    'Починаемо створення вакансії',
    'Starting creating new ad',
    'Начинаем составление новой вакансии'
]


what_need_to_do = [
'''
》<b>Для створення вакансії, вам необхідно пройти поетапно декілька наступних кроків:</b>

1) Вибрати країну та місто роботи
2) Вказати інформацію про заклад
3) Додати вакансію
4) Вказати додаткову інформацію, контактні дані, для зв'язку

Завершивши створення вакансії, є можливість переглянути ваше оголошення. При необхідності можете внести зміни.
''',
'''
<b>To create an ad, follow these steps:</b>

1) Select country and city
2) Enter the basic information of your establishment
3) Add a job, step by step
4) Specify additional information, contact details and so on.

Then you can review your advertisement and change any information if necessary
''',
'''
》<b>Чтобы создать объявление, вам необходимо пройти поэтапно несколько следующих шагов:</b>

1) Выбрать страну и город работы
2) Указать информацию заведения
3) Добавить вакансию 
4) Указать доп. информацию, контактные данные и т.д.

В самом конце можно посмотреть, как будет выглядеть ваше объявление, и при необходимости изменить любую информацию.
''']

choose_one_countree_lang = [
    'Оберіть країну:',
    'Select the country:',
    'Выберите одну из стран:'
]

create_ad_lang = [
    '📝 Створити повідомлення',
    '📝 Create ad',
    '📝 Создать объявление'
]

countrees_list = [
    ['Австрія', 'Austria', 'Австрия'],
    ['Бельгія', 'Belgium', 'Бельгия'],
    ['Болгарія', 'Bulgaria', 'Болгария'],
    ['Великобританія', 'United Kingdom', 'Великобритания'],
    ['Угорщина', 'Hungary', 'Венгрия'],
    ['Німеччина', 'Germany', 'Германия'],
    ['Греція', 'Greece', 'Греция'],
    ['Данія', 'Denmark', 'Дания'],
    ['Ірландія', 'Ireland', 'Ирландия'],
    ['Іспанія', 'Spain', 'Испания'],
    ['Італія', 'Italy', 'Италия'],
    ['Кіпр', 'Cyprus', 'Кипр'],
    ['Латвія', 'Latvia', 'Латвия'],
    ['Литва', 'Lithuania', 'Литва'],
    ['Люксембург', 'Luxembourg', 'Люксембург'],
    ['Мальта', 'Malta', 'Мальта'],
    ['Молдова', 'Moldova', 'Молдова'],
    ['Нідерланди', 'Netherlands', 'Нидерланды'],
    ['Польща', 'Poland', 'Польша'],
    ['Португалія', 'Portugal', 'Португалия'],
    ['Румунія', 'Romania', 'Румыния'],
    ['Словаччина', 'Slovakia', 'Словакия'],
    ['Словенія', 'Slovenia', 'Словения'],
    ['Фінляндія', 'Finland', 'Финляндия'],
    ['Франція', 'France', 'Франция'],
    ['Хорватія', 'Croatia', 'Хорватия'],
    ['Чехія', 'Czech Republic', 'Чехия'],
    ['Швейцарія', 'Switzerland', 'Швейцария'],
    ['Швеція', 'Sweden', 'Швеция'],
    ['Естонія', 'Estonia', 'Эстония']
]

countrees_flags = [
    '🇦🇹', '🇧🇪', '🇧🇬', '🇬🇧', '🇭🇺', '🇩🇪', '🇬🇷',
    '🇩🇰', '🇮🇪', '🇪🇸', '🇮🇹', '🇨🇾', '🇱🇻', '🇱🇹',
    '🇱🇺', '🇲🇹', '🇲🇩', '🇳🇱', '🇵🇱', '🇵🇹', '🇷🇴',
    '🇸🇰', '🇸🇮', '🇫🇮', '🇫🇷', '🇭🇷', '🇨🇿', '🇨🇭',
    '🇸🇪', '🇪🇪'
]

callbacks_list = [
    'austria', 'belgium', 'bulgaria', 'united_kingdom',
    'hungary', 'germany', 'greece', 'denmark',
    'ireland', 'spain', 'italy', 'cyprus',
    'latvia', 'lithuania', 'luxembourg', 'malta',
    'moldova', 'netherlands', 'poland', 'portugal',
    'romania', 'slovakia', 'slovenia', 'finland',
    'france', 'croatia', 'czech_republic', 'switzerland',
    'sweden', 'estonia'
]

you_choosed = [
    'Ви обрали ',
    'You choosed ',
    'Вы выбрали '
]

too_much_symbols = [
    'Забагато символів',
    'Too much symbols',
    'Слишком много символов'
]

choose_city = [
    'Введіть назву міста:',
    'Enter the city name:',
    'Введите название города:'
]

set_institytion_type_lang = [
'''
🏨 <b>Вкажіть тип закладу:</b>
(ресторан, бар, кафе, кав'ярня,
готель, кал’янна, хостел і т.д.)
''',
'''
🏨 <b>Specify your establishment type:</b>
(restaurant, motel, coffee house, pub,
cafe, hookah bar, hotel, fast-food)
''',
'''
🏨 <b>Укажите ваш тип заведения:</b>
(ресторан, бар, кафе, кофейня, отель,
кальянная, гостиница, паб и другое)
'''
]

set_institytion_name_lang = [
'''
⚜ <b>Вкажіть назву закладу:</b>
(приклад: Alaska, Jord, Catch, Azuma,
Fratelli, Goodman, Coast і так далі)
''',
'''
⚜ <b>Name of your institution:</b>
(for example: Alaska, Jord, Catch,
Azuma, Fratelli, Goodman, Coast, etc)
''',
'''
⚜ <b>Укажите название заведения:</b>
(пример: Alaska, Jord, Catch, Azuma,
Fratelli, Goodman, Coast и так далее)
'''
]

vacation_name = [
'''
👤 <b>Вкажіть назву вакансії:</b>
(кухар, офіціант, бармен, бариста,
посудомийниця, прибиральниця)
''',
'''
👤 <b>Specify the name of the vacancy:</b>
(cook, waiter, bartender, barista,
dishwasher, cleaner, courier and others)
''',
'''
👤 <b>Укажите название вакансии:</b>
(повар, официант, бармен, бариста,
посудомойщица, уборщица и т.д.)
'''
]

duties_lang = [
    'Обов\'язки працівника:',
    'Responsibilities of the incumbent:',
    'Обязанности сотрудника:'
]

requirements_lang = [
    'Вимоги до кандидата:',
    'Requirements for a job candidate:',
    'Требования к кандидату:'
]

job_conditions_lang = [
    'Умови роботи:',
    'Working conditions:',
    'Условия работы:'
]

contact_info_lang = [
'''
<b>Контактні дані:</b>
🗨 phone number, telegram link,
google forms, e-mail і так далі
''',
'''
<b>Contact information:</b>
🗨 phone number, telegram link,
e-mail, google forms, and others)
''',
'''
<b>Контактные данные:</b>
🗨 telegram link, phone number,
google forms, e-mail и т.д.
'''
]

share_phone_butt = [
    'Поділитися номером',
    'Share phone',
    'Отправить номер'
]

send_photo_lang = [
'''
🎞 <b>Надішліть фотографію:</b>
(горизонтальну або квадратну)
''',
'''
🎞 <b>Upload company the photo:</b>
(for example: horizontal or square)
''',
'''
🎞 <b>Отправьте фотографию:</b>
(горизонтальную или квадратную)'''
]

wrong_photo_lang = [    
'''
❌ <b>Невірний формат фото:</b>
(оріентація фотографії має бути
горизонтальною або квадратною)
''',
'''
❌ <b>Wrong photo format:</b>
(image may be landscape or square)
''',
'''
❌ <b>Не верный формат фото:</b>
(ориентация фото должна быть
горизонтальная или квадратная)
'''
]

edit_label_lang = [
    '🤔 Чи бажаєте ви змінити\n\
будь-яку інформацію в оголошенні?',
    '🤔 Would you like to change\n\
any information of the advertisement?',
    '🤔 Хотите ли вы изменить\n\
информацию в объявлении?'
]

edit_info_company = [
    'Інформація про компанію',
    'Company information',
    'Информация о компании'
]

edit_vacation = [
    'Вакансія',
    'Vacancy',
    'Вакансия'
]

edit_duties = [
    'Обов\'язки',
    'Duties',
    'Обязанности'
]

edit_requirments = [
    'Вимоги',
    'Requirements',
    'Требования'
]

edit_conditions = [
    'Умови',
    'Working conditions',
    'Условия'
]

edit_photo_logo = [
    'Логотип/фото',
    'Logo/photo',
    'Логотип/фото'
]

edit_contacts = [
    'Контакти',
    'Contacts',
    'Контакты'
]

edit_empty_vacation = [
    '🗑 Видалити',
    '🗑 Reset',
    '🗑 Удалить'
]

edit_accept = [
    '✅ Ні, все добре',
    '✅ No, all right!',
    '✅ Нет, все хорошо'
]

menu_create_vacation = [
    '📝 Створити Вакансію',
    '📝 Submit an ad',
    '📝 Создать Вакансию'
]

manu_share_chanel = [
    '🔄 Поширити канал',
    '🔄 Get this channel up',
    '🔄 Поделиться каналом'
]

menu_support = [
    '👩‍💻 Тех. Підтримка',
    '👩‍💻 Help',
    '👩‍💻 Тех. Поддержка'
]

send_to_the_moderators_lang = [
'''
📤 Ваше оголошення надіслано
на модерацію! Будь ласка,
очікуйте модерацію оголошення
адміністраторами каналу.

''',
'''
📤 Ad sent to moderation!
Please await review by
the channel admins.
''',
'''
📤 Объявление отправлено на
модерацию! Пожалуйста
ожидайте модерацию объявления
администраторами канала.
'''
]

post_confirmed_message = [
    '✅ Вітаємо! Ваше оголошення\n\
успішно пройшло модерацію,\n\
було схвалено та розміщено',
    '✅ Your ad was successful\n\
moderation. Ad posted',
    '✅ Поздравляем! Ваш пост\n\
успешно прошел модерацию,\n\
был одобрен и размещён'
]

clearing_all_lang = [
    'Видаляемо',
    'Reseting',
    'Сбрасываем'
]

share_chanel_lang = [
'''
✊ <b>Команда HoReCa Job UA</b> <a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🇺🇦</a>
не залишається байдужою, і 
створила для українців які 
були змушені залишити свої 
домівки у такій складний для 
всієї України та світу час, 
безкоштовні <a href='https://t.me/horecajobeu/3'>Телеграм-канали</a>
з підтримкою <a href='http://t.me/horecajobeubot'>чат-бота</a>, який 
допомагає знайти роботу за 
фахом у сфері гостинності
в інших країнах за кордоном.

Будемо вдячні, якщо ви зробите
сторіс, та напишете від себе 
текст про нас з посиланням на
телеграм-канал (за можливості).
Зараз допомога потрібна усім, 
тому це буде актуально та 
корисно для ваших підписників.

Посилання для сторіс –
<a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🗨</a> https://t.me/horecajobeu 
Зображення для сторіс ⤵️
''',
'''
✊ <b>Команда HoReCa Job UA</b> <a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🇺🇦</a>
не залишається байдужою, і 
створила для українців які 
були змушені залишити свої 
домівки у такій складний для 
всієї України та світу час, 
безкоштовні <a href='https://t.me/horecajobeu/3'>Телеграм-канали</a>
з підтримкою <a href='http://t.me/horecajobeubot'>чат-бота</a>, який 
допомагає знайти роботу за 
фахом у сфері гостинності
в інших країнах за кордоном.

Будемо вдячні, якщо ви зробите
сторіс, та напишете від себе 
текст про нас з посиланням на
телеграм-канал (за можливості).
Зараз допомога потрібна усім, 
тому це буде актуально та 
корисно для ваших підписників.

Посилання для сторіс –
<a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🗨</a> https://t.me/horecajobeu 
Зображення для сторіс ⤵️

''',
'''
✊ <b>Команда HoReCa Job UA</b> <a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🇺🇦</a>
не остается равнодушной, и
создала для украинцев которые
были вынуждены оставить
свои дома в такое сложное для
всей Украины и мира время,
бесплатные <a href='https://t.me/horecajobeu/3'>Телеграмм-каналы</a>
с поддержкой <a href='http://t.me/horecajobeubot'>чат-бота</a>, который
помогает найти работу в сфере
гостеприимства в странах ЕС

Будем вам благодарны, если 
вы сделаете сторис, и напишите
от себя текст о нас со ссылкой
на телеграмм-канал. Сейчас
помощь нужна всем, поэтому 
это будет актуально и полезно
для ваших подписчиков.

Ссылки для сторис –
<a href='https://telegra.ph/file/0bf2f0f902ee3029b7ce7.jpg'>🗨</a> https://t.me/horecajobeu 
Изображение для сторис ⤵️
'''
]

share_chanel_lang_send = [
'''

'''
]

tech_support_lang = [
'''
Тех пiдтримка
''',
'''
Tech support
''',
'''
Тех поддержка
'''
]

admin_damp = [
'📦 Дамп',
'📦 Memory dump',
'📦 Дамп'
]

admin_mail = [
'✉ Поширення',
'✉ Distribution',
'✉ Рассылка'
]

admin_message_lang = [
    'Введiть повiдомлення для розсилки',
    'Write message for distribution',
    'Введите сообщение для рассылки'
]

back_btn = [
    'Вiдмiна',
    'Back',
    'Отмена'
]

message_was_sended = [
    '✅ Повiдомленя було вiдправлено\n\
усiм користувачам',
    '✅ Message was sended to all users',
    '✅ Сообщение было отпралено\n\
всем пользователям чат-бота'
]

go_to_site_lang = [
    'Перейти на сайт',
    'Go to site',
    'Перейти на сайт'
]

share_chanel_button = [
    'Переслати',
    'Share',
    'Переслать'
]

no_answer = [
    'Такого варiанту нема',
    'No variant',
    'Такого варианта нету'
]
