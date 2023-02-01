import psycopg2
import os
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import csv
import codecs
import config


def create_table_users(sql_script="SELECT version();"):
    """просто выполняет переданный ей на вход скуль скрипт"""
    try:
        connection = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password,
                                      host=config.host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(sql_script)
        result = cursor
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка обращения к БД", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            result = "connection wasnt established"
    return result


def insert_users_into_table(list_users, sql_script="SELECT version();"):
    """просто выполняет переданный ей на вход скуль скрипт"""
    try:
        connection = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password,
                                      host=config.host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        for user in list_users:
            data = [int(user.user_employeeid), user.user_first_name, user.user_second_name, user.user_surname, int(user.user_age)]
            cursor.execute(sql_script, data)
        result = cursor
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка обращения к БД", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return result


def get_users_from_file(file_name):
    result = []
    fileobj = codecs.open(file_name, "r", "utf_8_sig")
    csv_reader = csv.reader(fileobj, delimiter=";")
    for row in csv_reader:
        user = config.User(user_employeeid=row[0], user_first_name=row[1],
                           user_second_name=row[2], user_surname=row[3], user_age=row[4])
        result.append(user)

    return result


def get_users_from_db(sql_script="SELECT version();"):
    try:
        result = []
        connection = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password,
                                      host=config.host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(sql_script)
        rows = cursor.fetchall()
        for row in rows:
            user = config.User(user_employeeid=row[0], user_first_name=row[1],
                               user_second_name=row[2], user_surname=row[3], user_age=row[4])
            result.append(user)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка обращения к БД", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return result


def get_one_user_from_db(userid):
    connection = None
    result = []
    try:
        connection = psycopg2.connect(dbname=config.dbname, user=config.user, password=config.password,
                                      host=config.host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"SELECT user_employeeid, user_first_name,"
                       f"user_second_name, user_surname, user_age FROM users where user_employeeid = {userid}")
        rows = cursor.fetchall()
        for row in rows:
            user = config.User(user_employeeid=row[0], user_first_name=row[1],
                               user_second_name=row[2], user_surname=row[3], user_age=row[4])
            result.append(user)
        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка обращения к БД", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
    return result
# create_table_users(config.create_table_users)
# list_users = get_users_from_file("Book1.csv")
# insert_users_into_table(list_users, config.insert_users_to_db)
print(get_users_from_db(config.select_all_users))
# for user in list_users:
#     user.display()

# print(get_one_user_from_db(7)[0].display())


