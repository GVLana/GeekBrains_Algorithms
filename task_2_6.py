"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


import random

def guess(n=random.randint(0, 100), count=0):
    check = input('Enter a number from 0 to 100: ')
    if check.isdigit():
        check = int(check)
        if check == n:
            print('You win!')
            return True
        if count > 10:
            print(f'You lost. The number was: {n}.')
            return True
        else:
            if check < n:
                print('Your guess is less than the number. Try again.')
            else:
                print('Your guess is bigger than the number. Try again.')
            count += 1
            return guess()

    else:
        print('You enter a string, not a number. Try again.')
        return guess()

guess()