# 0 - ua
# 1 - en
# 2 - ru


def check_lang(lang):
    print(lang)
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

what_need_to_do = ['''
》Чтобы создать объявление, вам необходимо
пройти поэтапно несколько следующих шагов:

1) Выбрать страну и город места работы
2) Указать основную информацию о заведении
3) Добавить вакансию поэтапно заполнив
4) Указать дополнительную
информацию/услуги/контакты и т.д.

В самом конце можно посмотреть, как будет
выглядеть ваше объявление, и при
необходимости изменить любую информацию

Выберите одну из стран:
''']

countrees_list = [
    ['🇦🇹 Австрія', '🇦🇹 Austria', '🇦🇹 Австрия'],
    ['🇧🇪 Бельгія', '🇧🇪 Belgium', '🇧🇪 Бельгия'],
    ['🇧🇬 Болгарія', '🇧🇬 Bulgaria', '🇧🇬 Болгария'],
    ['🇬🇧 Великобританія', '🇬🇧 United Kingdom', '🇬🇧 Великобритания'],
    ['🇭🇺 Угорщина', '🇭🇺 Hungary', '🇭🇺 Венгрия'],
    ['🇩🇪 Німеччина', '🇩🇪 Germany', '🇩🇪 Германия'],
    ['🇬🇷 Греція', '🇬🇷 Greece', '🇬🇷 Греция'],
    ['🇩🇰 Данія', '🇩🇰 Denmark', '🇩🇰 Дания'],
    ['🇮🇪 Ірландія', '🇮🇪 Ireland', '🇮🇪 Ирландия'],
    ['🇪🇸 Іспанія', '🇪🇸 Spain', '🇪🇸 Испания'],
    ['🇮🇹 Італія', '🇮🇹 Italy', '🇮🇹 Италия'],
    ['🇨🇾 Кіпр', '🇨🇾 Cyprus', '🇨🇾 Кипр'],
    ['🇱🇻 Латвія', '🇱🇻 Latvia', '🇱🇻 Латвия'],
    ['🇱🇹 Литва', '🇱🇹 Lithuania', '🇱🇹 Литва'],
    ['🇱🇺 Люксембург', '🇱🇺 Luxembourg', '🇱🇺 Люксембург'],
    ['🇲🇹 Мальта', '🇲🇹 Malta', '🇲🇹 Мальта'],
    ['🇲🇩 Молдова', '🇲🇩 Moldova', '🇲🇩 Молдова'],
    ['🇳🇱 Нідерланди', '🇳🇱 Netherlands', '🇳🇱 Нидерланды'],
    ['🇵🇱 Польща', '🇵🇱 Poland', '🇵🇱 Польша'],
    ['🇵🇹 Португалія', '🇵🇹 Portugal', '🇵🇹 Португалия'],
    ['🇷🇴 Румунія', '🇷🇴 Romania', '🇷🇴 Румыния'],
    ['🇸🇰 Словаччина', '🇸🇰 Slovakia', '🇸🇰 Словакия'],
    ['🇸🇮 Словенія', '🇸🇮 Slovenia', '🇸🇮 Словения'],
    ['🇫🇮 Фінляндія', '🇫🇮 Finland', '🇫🇮 Финляндия'],
    ['🇫🇷 Франція', '🇫🇷 France', '🇫🇷 Франция'],
    ['🇭🇷 Хорватія', '🇭🇷 Croatia', '🇭🇷 Хорватия'],
    ['🇨🇿 Чехія', '🇨🇿 Czech Republic', '🇨🇿 Чехия'],
    ['🇨🇭 Швейцарія', '🇨🇭 Switzerland', '🇨🇭 Швейцария'],
    ['🇸🇪 Швеція', '🇸🇪 Sweden', '🇸🇪 Швеция'],
    ['🇪🇪 Естонія', '🇪🇪 Estonia', '🇪🇪 Эстония'],
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
