# Imports
from assets import database as db
from assets.language_list import *


def data_beautify_bd(data):
    if isinstance(data, str):
        return f'"{data}"'
    return f'{data}'


def get_full_post(usr_id, lang):
    _country = db.get_post_data(usr_id, 'country')
    _city = db.get_post_data(usr_id, 'city').title().replace(' ', '_')

    if lang == 0:  # ua
        return f'''
{countrees_flags[callbacks_list.index(_country)]} #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type')}, {db.get_post_data(usr_id, 'institution_name')}

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Обов'язки працівника:
{db.get_post_data(usr_id, 'duties')}

Вимоги до кандидата:
{db.get_post_data(usr_id, 'requirements')}

Умови роботи:
{db.get_post_data(usr_id, 'job_conditions')}

Контактні дані:
{db.get_post_data(usr_id, 'contact_info')}
'''

    if lang == 1:  # en
        return f'''
{countrees_flags[callbacks_list.index(_country)]} #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type')}, {db.get_post_data(usr_id, 'institution_name')}

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Responsibilities of the incumbent:
{db.get_post_data(usr_id, 'duties')}

Requirements for a job candidate:
{db.get_post_data(usr_id, 'requirements')}

Working conditions:
{db.get_post_data(usr_id, 'job_conditions')}

Contact information:
{db.get_post_data(usr_id, 'contact_info')}
'''

    if lang == 2:  # ru
        return f'''
{countrees_flags[callbacks_list.index(_country)]} #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))].replace(' ', '_')}, #{_city}
{db.get_post_data(usr_id, 'institution_type')}, {db.get_post_data(usr_id, 'institution_name')}

》<b>{db.get_post_data(usr_id, 'job_name').title()}</b>

Обязаности сотрудника:
{db.get_post_data(usr_id, 'duties')}

Требования к кандидату:
{db.get_post_data(usr_id, 'requirements')}

Условия работы:
{db.get_post_data(usr_id, 'job_conditions')}

Контактные данные:
{db.get_post_data(usr_id, 'contact_info')}
'''