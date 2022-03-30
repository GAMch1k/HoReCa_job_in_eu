# Imports
from assets import database as db
from assets.language_list import *


def data_beautify_bd(data):
    if isinstance(data, str):
        return f'"{data}"'
    return f'{data}'


def get_full_post(usr_id):
    _country = db.get_post_data(usr_id, 'country')
    _city = db.get_post_data(usr_id, 'city')

    _post = f'''
{countrees_flags[callbacks_list.index(_country)]} #{countrees_list[callbacks_list.index(_country)][check_lang(db.get_user_lang(usr_id))]}, #{_city.title()}
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
    return _post

# print(get_full_post(532666364))