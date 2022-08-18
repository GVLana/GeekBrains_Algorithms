"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

data_login = {'Thor': 'bhbj125', 'Loki': 'nfvjfk15', 'Odin': 'vnfdunv89', 'Spiderman': 'kjfnjkgfn45', 'Wonderwoman': 'fvniof45dh'}
data_status = {'Thor': 1, 'Wonderwoman': 0, 'Loki': 1, 'Odin': 0, 'Spiderman': 0}

user_input = input('Enter your login: ')

# вар1 Сложность O(1)
def signup(x):                                                                          #O(1)
    new_user = input('Create your login name: ')                                        #O(1)
    new_password = input('Create your password: ')                                      #O(1)
    data_login[new_user] = new_password                                                 #O(1)
    data_status[new_user] = 1                                                           #O(1)
    return data_login, data_status                                                      #O(1)

# def check_user(db):
#     if user_input in data_status and data_status[user_input] == 1:                      #O(1)
#         password = input('Enter your password: ')                                       #O(1)
#         count = 0                                                                       #O(1)
#         while password != data_login[user_input] and count != 5:                        #O(1)
#             print('Incorrect password. Please try again.')                              #O(1)
#             password = input('Enter your password: ')                                   #O(1)
#             count += 1                                                                  #O(1)
#         if count == 5:                                                                  #O(1)
#             data_status[user_input] = 0                                                 #O(1)
#             print('Too many attempts. Your account was blocked.')                       #O(1)
#             return data_status                                                          #O(1)
#         else:
#             print('Hello!')                                                             #O(1)
#     elif user_input in data_status and data_status[user_input] == 0:                    #O(1)
#         print('Your account has been deactivated. Please, signup again.')               #O(1)
#         return signup(user_input)                                                       #O(1)
#
#     else:
#         print('There is no such account. Please, signup again.')                        #O(1)
#         return signup(user_input)                                                       #O(1)
#
# print(check_user(user_input))

# вар2 Сложность O(N)
def check_user_2(db):
    for k, v in data_status.items():                                                        #O(N)
        if user_input == k and data_status[k] == 1:                                         #O(1)
            password = input('Enter your password: ')                                       #O(1)
            count = 0                                                                       #O(1)
            while password != data_login[user_input] and count != 5:                        #O(1)
                print('Incorrect password. Please try again.')                              #O(1)
                password = input('Enter your password: ')                                   #O(1)
                count += 1                                                                  #O(1)
            if count == 5:                                                                  #O(1)
                data_status[user_input] = 0                                                 #O(1)
                print('Too many attempts. Your account was blocked.')                       #O(1)
                return data_status                                                          #O(1)
            else:
                print('Hello!')                                                             #O(1)
                break                                                                       #O(1)
        elif user_input == k and data_status[k] == 0:                                       #O(1)
            print('Your account has been deactivated. Please, signup again.')               #O(1)
            return signup(user_input)                                                       #O(1)

        else:
            print('There is no such account. Please, signup again.')                        #O(1)
            return signup(user_input)                                                       #O(1)

print(check_user_2(user_input))