"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""


def check_equation(n):
    if n == 1:
        return n
    else:
        return check_equation(n-1) + n

#
# try:
#     user_input = input('Enter a natural number: ')
#     if user_input.isdigit() and user_input != '0':
#         num = int(user_input)
#         if check_equation(num) == num * (num + 1) / 2:
#             print('The equality is true.')
#         else:
#             print('The equality is false.')
#     elif user_input == '0':
#         print(f'{user_input} is not valid option. Try again.')
#     else:
#         print('You enter a string, not a number. Try again.')
# except ValueError:
#     print('Something went wrong.')


try:
    user_input = int(input('Enter a natural number, starts from 1: '))
    if check_equation(user_input) == user_input * (user_input + 1) / 2:
        print('The equality is true.')
    else:
        print('The equality is false.')
except ValueError:
    print('You enter a string, not a number. Try again.')

