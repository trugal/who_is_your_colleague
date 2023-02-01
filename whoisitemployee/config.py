class User:
    def __init__(self, user_employeeid, user_first_name, user_second_name, user_surname, user_age):
        self.user_employeeid = user_employeeid
        self.user_first_name = user_first_name
        self.user_second_name = user_second_name
        self.user_surname = user_surname
        self.user_age = user_age

    def display(self):
        print(self.user_employeeid)
        print(self.user_first_name)
        print(self.user_second_name)
        print(self.user_surname)
        print(self.user_age)

    def get_user(self):
        result = {'user_employeeid': self.user_employeeid, 'user_first_name': self.user_first_name,
                  'user_second_name': self.user_second_name, 'user_surname': self.user_surname,
                  'user_age': self.user_age}
        return result


dbname = 'suppliers'
user = 'user1'
password = 'Qwerty!23'
host = 'localhost'

create_table_users = """
CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
user_employeeid INTEGER NOT NULL,
user_first_name VARCHAR(255) NOT NULL,
user_second_name VARCHAR(255) NOT NULL,
user_surname VARCHAR(255) NOT NULL,
user_age INTEGER NOT NULL
)
"""

select_all_users = """
SELECT * FROM users
"""
select_one_user = """
SELECT * FROM users
where user_employeeid = %s
"""

insert_users_to_db = """
INSERT INTO users (user_employeeid, user_first_name, user_second_name, user_surname, user_age)
VALUES (%s, %s, %s, %s, %s)
"""