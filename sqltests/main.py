# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import psycopg2
import re
import datetime


class User:
    def __init__(self, fname, sname, lname,  bdate):
        self.fname=fname
        self.sname = sname
        self.lname=lname
        self.bdate=bdate


conn = psycopg2.connect(
    host="localhost",
    database="suppliers",
    user="postgres",
    password="Pla100r!")
list_of_users = []
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:

    current_user = User(fname=row[1], sname=row[2], lname=row[3], bdate=row[4])
    list_of_users.append(current_user)
    print(vars(current_user))
print(*list_of_users)

# list_fname = ["Iwan", "Petr", "Veniamin"]
# list_sname = ["Petrovich", "Veniaminovich", "Iwanovich"]
# list_lname = ["Veniaminov", "Iwanov", "Petrov"]
# list_bdate = ["10-10-2000", "1-1-2010", "11-11-2020"]
# command = """CREATE TABLE IF NOT EXISTS users (
#             user_id SERIAL PRIMARY KEY,
#             user_name VARCHAR(255) NOT NULL
#             )"""
# command = """ INSERT INTO users (first_name, second_name, surname, birthdate)
# VALUES(%s, %s, %s, %s);
#  """
# command = """ALTER TABLE users
# ADD COLUMN first_name VARCHAR(255),
# ADD COLUMN second_name VARCHAR(255),
# ADD COLUMN surname VARCHAR(255),
# ADD COLUMN birthdate DATE;
# """
# command =""" ALTER TABLE users
#  DROP COLUMN user_name;
#  """
# command = """DELETE FROM users
# where user_id IS NOT NULL;"""
# command = """ALTER TABLE users
# ALTER COLUMN first_name SET NOT NULL,
# ALTER COLUMN second_name SET NOT NULL,
# ALTER COLUMN surname SET NOT NULL,
# ALTER COLUMN birthdate SET NOT NULL;
# """
# dict = ["user1", "user2", "user3"]
# for i in range(len(list_fname)):
#     data = (list_fname[i], list_sname[i], list_lname[i], list_bdate[i])
#     cursor.execute(command, data)
# cursor.execute(command)
cursor.close()
conn.commit()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
