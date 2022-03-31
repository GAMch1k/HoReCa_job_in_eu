from assets import database as db


def main():
    print('Telegram id можно взять у @getmyid_bot или из базы данных')
    user_id = int(input('Введите telegram id пользователя: '))
    give = int(input('Дать или забрать роль админа? (Введите только цифру)\n\
1 - Дать\n2 - Забрать\n'))

    if user_id:
        if give == 1:
            db.set_user_admin(user_id, True)
            print('Роль администратора выдана')
        elif give == 2:
            db.set_user_admin(user_id, False)
            print('Роль администратора забрана')
        else:
            wrong_data()
    else:
        wrong_data()

def wrong_data():
    print('Какое-то значение не верно')

main()
