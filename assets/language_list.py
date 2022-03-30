# 0 - ua
# 1 - en
# 2 - ru


def check_lang(lang):
    if (lang == 'ua'): return 0
    if (lang == 'en'): return 1
    return 2


welcome_message = '''
HoReCa | Job in EU – створено
для допомоги людям із України.
Тут ви можете надати роботу для
українців в інших країнах.

HoReCa | Job in EU – создан для
помощи людям из Украины. Здесь
вы можете предоставить работы
для украинцев в других странах.

HoReCa | Job in EU – created to
help people from Ukraine. Here you
can provide jobs for Ukrainians in
other countries.
'''

choose_language = '''
Оберіть будь ласка мову бота
для зручної комунікації.

Выберите пожалуйста язык
бота для удобной коммуникации.

Select please the bot language
for easy communication.
'''

what_need_to_do = [
'''
》Для створення вакансії, вам необхідно
пройти поетапно декілька наступних кроків:

1) Вибрати країну та місто місця роботи
2) Вказати основну інформацію про заклад
3) Додати вакансію, поетапно заповнивши
4) Вказати додатковуінформацію/послуги/контакти тощо.

Завершивши створення вакансії, є можливість переглянути ваше оголошення.
При необхідності можна внести зміни

Оберіть країну:
''',
'''
》To create an ad, follow these steps:

1) Select the country and city of workplace
2) Specify the main information establishment
3) Add a vacancy by filling it in stages
4) Specify the additional information/service/contacts, and others.

Then you can review your advertisement and change any information if necessary

Select the country:
''',
'''
》Чтобы создать объявление, вам необходимо
пройти поэтапно несколько следующих шагов:

1) Выбрать страну и город места работы
2) Указать основную информацию о заведении
3) Добавить вакансию поэтапно заполнив
4) Указать дополнительную информацию/услуги/контакты и т.д.

В самом конце можно посмотреть, как будет выглядеть ваше объявление, и при необходимости изменить любую информацию

Выберите одну из стран:
''']

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

choose_city = [
    'Введіть назву міста:',
    'Enter the city name:',
    'Введите название города:'
]

set_institytion_type_lang = [
'''
🏨 Вкажіть тип закладу:
(ресторан, бар, кафе, кав'ярня, готель, кал’янна, хостел, паб, фаст-фуд і т.д)
''',
'''
🏨 Specify your establishment type:
(restaurant, pub, cafe, coffee house, motel, hookah bar, hotel, fast-food and others)
''',
'''
🏨 Укажите ваш тип заведения:
(ресторан, бар, кафе, кофейня, отель, кальянная, гостиница, паб и другое)
'''
]

set_institytion_name_lang = [
'''
⚜ Вкажіть назву закладу:
(приклад: Alaska, Jord, Catch, Azuma, Fratelli, Goodman, Coast і так далі)
''',
'''
⚜ Specify the name of the establishment:
(for example: Alaska, Jord, Catch, Azuma, Fratelli, Goodman, Coast, etc)
''',
'''
⚜ Укажите название заведения
(пример: Alaska, Jord, Catch, Azuma, Fratelli, Goodman, Coast и так далее)
'''
]

vacation_name = [
'''
👤 Вкажіть назву вакансії:
(кухар, офіціант, бармен, бариста, посудомийниця, прибиральниця)
''',
'''
👤 Specify the name of the vacancy:
(cook, waiter, bartender, barista, dishwasher, cleaner, courier and others)
''',
'''
👤 Укажите название вакансии:
(повар, официант, бармен, бариста, посудомойщица, уборщица и т.д.)
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
Контактні дані:
🗨 phone number, telegram link, google forms, e-mail і так далі
''',
'''
Contact information:
🗨 phone number, telegram link, google forms, e-mail, and others)
''',
'''
Контактные данные:
🗨 phone number, e-mail, telegram link, google forms и так далее
'''
]

send_photo_lang = [
'''
🎞 Надішліть фотографію:
(горизонтальну або квадратну)
''',
'''
🎞 Upload company the photo:
(for example: horizontal or square)
''',
'''
🎞 Отправьте фотографию:
(горизонтальную или квадратную)'''
]

edit_label_lang = [
    '🤔 Чи бажаєте ви змінити будь-яку інформацію в оголошенні?',
    '🤔 Would you like to change any information of the advertisement?',
    '🤔 Хотите ли вы изменить какую-либо информацию в данном объявлении?'
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
    '🗑 Сброс заполнения вакансии'
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
    '󰠁 Тех. Підтримка',
    '󰠁 Help',
    '󰠁 Тех. Поддержка'
]

send_to_the_moderators_lang = [
'''
Оголошення надіслано на модерацію!
Будь ласка, очікуйте модерації оголошення адміністраторами каналу HoReCa Job EU
''',
'''
The advertisement was sent to the
moderation! Please, wait a while, the answer will be sent to you so quickly as it is possible.
''',
'''
Объявление отправлено на модерацию!
Пожалуйста ожидайте модерацию объявления администраторами канала
'''
]

post_confirmed_message = [
    '✅ Ваш пост успішно пройшов модерацію, був схвалений та розміщений на каналі',
    '✅ Your advertisement has passed the moderation successfully. The advert has appeared on our Telegram channel.',
    '✅ Ваш пост успешно прошел модерацию, был одобрен и размещен на канале'
]

clearing_all_lang = [
    'Видаляемо',
    'Reseting',
    'Сбрасываем'
]

share_chanel_lang = [
'''
Розшарити канал
''',
'''
Share chanel
''',
'''
Поделится каналом
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
