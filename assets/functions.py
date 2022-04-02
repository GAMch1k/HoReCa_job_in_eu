# Imports
from assets import database as db
from assets.language_list import *

from telegraph import Telegraph
from bs4 import BeautifulSoup as bs
import requests
import os

telegraph = Telegraph()
telegraph.create_account(short_name='1234')

def get_image_telegraph(img_id):
    with open(f'assets/images/{img_id}.jpg', 'rb') as f:
        path = requests.post('https://telegra.ph/upload', files={'file': ('file', f, 'image/jpg')}).json()[0]['src']
    response = telegraph.create_page('HoReCa', html_content=f'<img src=\'{path}\'/>')

    link = response['url']
    req = requests.get(link)

    data = bs(req.text, 'html.parser')
    img = data.find_all('img', src=True)

    img_src = [x['src'] for x in img]
    # os.remove(f'assets/images/{img_id}.jpg')
    # print('https://telegra.ph' + img_src[0])
    return 'https://telegra.ph' + img_src[0]



def data_beautify_bd(data):
    if isinstance(data, str):
        return f'"{data}"'
    return f'{data}'


def get_full_post(usr_id, lang, post_id=None):
    if post_id == None:
        _country = db.get_post_data(usr_id, 'country')
        _city = db.get_post_data(usr_id, 'city').title().replace(' ', '_')

        if lang == 0:  # ua
            return f'''
<a href='{get_image_telegraph(db.get_post_data(usr_id, 'id'))}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type').title()} «{db.get_post_data(usr_id, 'institution_name').title()}»

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Обов'язки працівника:
- {db.get_post_data(usr_id, 'duties').lower()}

Вимоги до кандидата:
- {db.get_post_data(usr_id, 'requirements').lower()}

Умови роботи:
- {db.get_post_data(usr_id, 'job_conditions').lower()}

Контактні дані:
🗨 {db.get_post_data(usr_id, 'contact_info')}
'''

        if lang == 1:  # en
            return f'''
<a href='{get_image_telegraph(db.get_post_data(usr_id, 'id'))}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type').title()} «{db.get_post_data(usr_id, 'institution_name').title()}»

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Responsibilities of the incumbent:
- {db.get_post_data(usr_id, 'duties').lower()}

Requirements for a job candidate:
- {db.get_post_data(usr_id, 'requirements').lower()}

Working conditions:
- {db.get_post_data(usr_id, 'job_conditions').lower()}

Contact information:
🗨 {db.get_post_data(usr_id, 'contact_info')}
'''

        if lang == 2:  # ru
            return f'''
<a href='{get_image_telegraph(db.get_post_data(usr_id, 'id'))}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type').title()} «{db.get_post_data(usr_id, 'institution_name').title()}»

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Обязанности сотрудника:
- {db.get_post_data(usr_id, 'duties').lower()}

Требования к кандидату:
- {db.get_post_data(usr_id, 'requirements').lower()}

Условия работы:
- {db.get_post_data(usr_id, 'job_conditions').lower()}

Контактные данные:
🗨 {db.get_post_data(usr_id, 'contact_info')}
'''
    else:
        print('GETTING POST')
        _country = db.get_post_data(0, 'country', post_id)
        _city = db.get_post_data(0, 'city', post_id).title().replace(' ', '_')

        if lang == 0:  # ua
            return f'''
<a href='{get_image_telegraph(post_id)}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type', post_id).title()} «{db.get_post_data(usr_id, 'institution_name', post_id).title()}»

》<b>{db.get_post_data(usr_id, 'job_name', post_id).title()}</b>

Обов'язки працівника:
- {db.get_post_data(usr_id, 'duties', post_id).lower()}

Вимоги до кандидата:
- {db.get_post_data(usr_id, 'requirements', post_id).lower()}

Умови роботи:
- {db.get_post_data(usr_id, 'job_conditions', post_id).lower()}

Контактні дані:
🗨 {db.get_post_data(usr_id, 'contact_info', post_id)}
'''

        if lang == 1:  # en
            return f'''
<a href='{get_image_telegraph(post_id)}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type', post_id).title()} «{db.get_post_data(usr_id, 'institution_name', post_id).title()}»

》<b>{db.get_post_data(usr_id, 'job_name', post_id).title()}</b>

Responsibilities of the incumbent:
- {db.get_post_data(usr_id, 'duties', post_id)}

Requirements for a job candidate:
- {db.get_post_data(usr_id, 'requirements', post_id)}

Working conditions:
- {db.get_post_data(usr_id, 'job_conditions', post_id)}

Contact information:
🗨 {db.get_post_data(usr_id, 'contact_info', post_id)}
'''

        if lang == 2:  # ru
            return f'''
<a href='{get_image_telegraph(post_id)}'>{countrees_flags[callbacks_list.index(_country)]}</a> #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type', post_id).title()} «{db.get_post_data(usr_id, 'institution_name', post_id).title()}»

》<b>{db.get_post_data(usr_id, 'job_name', post_id).title()}</b>

Обязанности сотрудника:
- {db.get_post_data(usr_id, 'duties', post_id)}

Требования к кандидату:
- {db.get_post_data(usr_id, 'requirements', post_id)}

Условия работы:
- {db.get_post_data(usr_id, 'job_conditions', post_id)}

Контактные данные:
🗨 {db.get_post_data(usr_id, 'contact_info', post_id)}
'''