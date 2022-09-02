"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

from hashlib import sha256
import sqlite3

class LogInfo:
    def __init__(self):
        self.conn = sqlite3.connect('us_info.db')
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS users_info (login varchar(255) UNIQUE, password varchar(255));")
        self.conn.commit()


    @staticmethod
    def to_hash():
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        hash_obj = sha256(login.encode() + password.encode()).hexdigest()
        return login, hash_obj

    def sign_up(self):
        login, to_hash = self.to_hash()
        user_info = (login, to_hash)
        self.cur.execute("INSERT INTO users_info (login, password) VALUES(?, ?);", user_info)
        self.conn.commit()

    def sign_in(self):
        login, to_check = self.to_hash()
        self.cur.execute("SELECT password FROM users_info WHERE login = ?;", (login,))
        one_result = self.cur.fetchone()
        if one_result and to_check == one_result[0]:
            print('Welcome back!')
        else:
            print('There is no such match. Please try again or sign up.')

    def print_in(self):
        self.cur.execute("SELECT * FROM users_info")
        three_results = self.cur.fetchmany(3)
        print(three_results)

test = LogInfo()
test.create_table()
# test.sign_up()
test.print_in()
# test.sign_in()


