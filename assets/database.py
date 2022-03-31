# Database functions

# Imports
import sqlite3
from assets import functions
from xlsxwriter.workbook import Workbook
# import pandas as pd


# Creating connection to database
db = sqlite3.connect('assets/database/horeca.db', check_same_thread=False)


def new_post(user_id, country):
    try:
        # Creating cursor
        cur = db.cursor()

        # Adding new post to the database
        cur.execute(f'''INSERT INTO "posts" (
            creator_id,
            country,
            mods_approved,
            editing
        ) VALUES (
            {user_id},
            "{country}",
            {False},
            {False}
        )''')

        db.commit()

    except sqlite3.Error as er:
        print('NEW POST CREATION ERROR')
        print(er)


def dump_to_excel():
    try:
        workbook = Workbook('assets/database/excel_db.xlsx')
        worksheet = workbook.add_worksheet()

        # Creating cursor
        cur = db.cursor()
        # Getting data
        cur.execute('SELECT * FROM "users"')
        mysel = cur.execute('SELECT * FROM "users"')

        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()

    except Exception as e:
        print(e)
        print('DATABASE DUMP TO EXCEL ERROR')


def change_user_language(user_id, language):
    try:
        # Creating cursor
        cur = db.cursor()

        # changing language
        cur.execute(f'''UPDATE "users" SET "lang" = "{language}" WHERE "user_id" = {user_id}''')

        db.commit()

    except sqlite3.Error as er:
        print('CHANGE USER LANGUAGE ERROR')
        print(er)


def get_post_data(user_id, value, post_id=None):
    if post_id == None:
        try:
            # Creating cursor
            cur = db.cursor()
        
            # Getting data
            cur.execute(f'''SELECT "{value}" from "posts" WHERE "creator_id" = {user_id} AND "id" = (SELECT max(id) FROM "posts" WHERE "creator_id" = {user_id})''')
            return cur.fetchall()[0][0]

        except sqlite3.Error as er:
            print('GET POST DATA ERROR')
            print(er)
    else:
        try:
            # Creating cursor
            cur = db.cursor()
        
            # Getting data
            cur.execute(f'''SELECT "{value}" from "posts" WHERE "id" = {post_id}''')
            return cur.fetchall()[0][0]

        except sqlite3.Error as er:
            print('GET POST DATA ERROR')
            print(er)


def update_post_value(user_id, value, data):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # updating last post data 
        cur.execute(f'''UPDATE "posts" SET "{value}" = {functions.data_beautify_bd(data)} WHERE "creator_id" = {user_id} AND "id" = (SELECT max(id) FROM "posts" WHERE "creator_id" = {user_id})''')

        db.commit()

    except sqlite3.Error as er:
        print('UPDATE POST DATA ERROR')
        print(er)


def delete_last_users_post(user_id):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # updating last post data 
        cur.execute(f'''DELETE FROM "posts" WHERE "creator_id" = {user_id} AND "id" = (SELECT max(id) FROM "posts" WHERE "creator_id" = {user_id})''')

        db.commit()

    except sqlite3.Error as er:
        print('DELETE LAST POST DATA ERROR')
        print(er)


def is_post_editing(user_id):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # getting post data 
        cur.execute(f'''SELECT "editing" from "posts" WHERE "creator_id" = {user_id} AND "id" = (SELECT max(id) FROM "posts" WHERE "creator_id" = {user_id})''')

        return cur.fetchall()[0][0]

    except sqlite3.Error as er:
        print('GETTING EDITING POST DATA ERROR')
        print(er)


# Getting users last post id
def get_post_id(user_id):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # getting post data 
        cur.execute(f'''SELECT "id" from "posts" WHERE "creator_id" = {user_id} AND "id" = (SELECT max(id) FROM "posts" WHERE "creator_id" = {user_id})''')

        return cur.fetchall()[0][0]

    except sqlite3.Error as er:
        print('GETTING POST ID ERROR')
        print(er)


# Getting post id
def get_user_id_by_post_id(post_id):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # getting post data 
        cur.execute(f'''SELECT "creator_id" from "posts" WHERE "id" = {post_id}''')

        return cur.fetchall()[0][0]

    except sqlite3.Error as er:
        print('GETTING POST ID ERROR')
        print(er)


def new_user(user_id, language, is_admin=False):
    try:
        # Creating cursor
        cur = db.cursor()

        # Adding user to the database
        cur.execute(f'''INSERT INTO "users" VALUES (
            {user_id},
            "{language}",
            {is_admin},
            "{''}"
        )''')

        db.commit()

    except sqlite3.Error as er:
        print('NEW USER CREATION ERROR')
        print(er)


def update_user_value(user_id, value, data):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # updating user data 
        cur.execute(f'''UPDATE "users" SET "{value}" = "{data}" WHERE "user_id" = {user_id}''')

        db.commit()

    except sqlite3.Error as er:
        print('UPDATE USER DATA ERROR')
        print(er)


def set_user_admin(user_id, is_admin):
    try:
        # Creating cursor
        cur = db.cursor()
        
        # updating last post data 
        cur.execute(f'''UPDATE "users" SET "is_admin" = {is_admin} WHERE "user_id" = {user_id}''')

        db.commit()

    except sqlite3.Error as er:
        print('SET USER ADMIN ERROR')
        print(er)


def get_user_lang(user_id):
    try:
        # Creating cursor
        cur = db.cursor()
        if id:
            # Getting data
            cur.execute(f'''SELECT "lang" from "users" WHERE "user_id" = {user_id}''')
            return cur.fetchall()[0][0]

    except sqlite3.Error as er:
        print('GET USER LANGUAGE ERROR')
        print(er)


def is_user_admin(user_id):
    try:
        # Creating cursor
        cur = db.cursor()

        # Getting data
        cur.execute(f'''SELECT "is_admin" from "users" WHERE "user_id" = {user_id}''')
        return cur.fetchall()[0][0]

    except sqlite3.Error as er:
        print('GETING ADMIN STATE ERROR')
        print(er)


# Just print all users
def print_all_users():
    cur = db.cursor()
    cur.execute('SELECT * FROM "users"')
    print(cur.fetchall())


# Just print all posts
def print_all_posts():
    cur = db.cursor()
    cur.execute('SELECT * FROM "posts"')
    print(cur.fetchall())


def init():
    # Creating cursor
    cur = db.cursor()

    # Creating tables if they aren't exists
    cur.execute('''CREATE TABLE if not exists "users" (
    "user_id" INTEGER PRIMARY KEY,
    "lang" CHAR(2) NOT NULL,
    "is_admin" BOOLEAN NOT NULL,
    "contact_info" CHAR(100))
    ''')
    cur.execute('''CREATE TABLE if not exists "posts" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "creator_id" INTEGER NOT NULL,
    "country" CHAR(30),
    "city" CHAR(30),
    "institution_type" CHAR(30),
    "institution_name" CHAR(40),
    "job_name" CHAR(30),
    "duties" CHAR(250),
    "requirements" CHAR(250),
    "job_conditions" CHAR(250),
    "contact_info" CHAR(100),
    "mods_approved" BOOLEAN NOT NULL,
    "editing" BOOLEAN NOT NULL,
    "mods_chat_id" INTEGER
    )''')
    db.commit()

init()
