"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd(num, e_count=0, odd_count=0):
    if num == 0:
        print("Количество четных и нечетных цифр в числе равно: ")
        return e_count, odd_count
    else:
        check = num % 10
        num = num // 10
        if check % 2 == 0:
            e_count += 1
        else:
            odd_count += 1
        return even_odd(num, e_count, odd_count)


try:
    user_input = int(input("Enter a natural number: "))
    print(f'{even_odd(user_input)}')
except ValueError:
    print('You enter a string not a number. Try again.')

