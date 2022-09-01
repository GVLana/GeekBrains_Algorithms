"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sequense_sum(n_count, n, i=0, n_sum=0):
    if i == n_count:
        print(f'The sequence length is {n_count}. The total sum is {n_sum}.')
        return " "
    else:
        i += 1
        n_sum += n
        return sequense_sum(n_count, n/2*-1, i, n_sum)

try:
    user_input = int(input('Enter the number - the length of the sequence: '))
    sequense_sum(user_input, 1)
except ValueError:
    print('You enter a string, not a number. Try again.')

