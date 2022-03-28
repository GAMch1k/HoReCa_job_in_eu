# Database functions

# Imports
import sqlite3


# Creating connection to database
db = sqlite3.connect('assets/database/horeca.db', check_same_thread=False)


def new_user(user_id, language, is_admin=False):
    try:
        # Creating cursor
        cur = db.cursor()

        # Adding user to the database
        cur.execute(f'''INSERT INTO "users" VALUES (
            {user_id},
            "{language}",
            {is_admin}
        )''')

        db.commit()

    except sqlite3.Error as er:
        print('NEW USER CREATION ERROR')
        print(er)
    print_all_users()
    

# Just print all users
def print_all_users():
    cur = db.cursor()
    cur.execute('SELECT * FROM users')
    print(cur.fetchall())


def init():
    # Creating cursor
    cur = db.cursor()

    # Creating tables if they aren't exists
    cur.execute('''CREATE TABLE if not exists "users" (
    "user_id" INTEGER PRIMARY KEY,
    "lang" CHAR(2) NOT NULL,
    "is_admin" BOOLEAN NOT NULL)
    ''')
    cur.execute('''CREATE TABLE if not exists "posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "creator_id" INTEGER NOT NULL,
    "country" CHAR(50),
    "city" CHAR(50),
    "institution_type" CHAR(50),
    "institution_name" CHAR(80),
    "job_name" CHAR(50),
    "duties" CHAR(700),
    "contact_info" CHAR(300),
    "image_id" INTEGER,
    "mods_approved" BOOLEAN NOT NULL
    )''')
    db.commit()

init()
