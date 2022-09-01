"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""

from timeit import timeit

test = [i for i in range(10000)]

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# print(func_1(test))


#list comprehension - тоже использует цикл for но выигрывает по скорости т.к. не вызывает метод append у списка
def func_2(nums):
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr

# print(func_2(test))



#замеры времени:

print('Замер времени для func_1: ', timeit("func_1(test[:])", globals=globals(), number=1000))

print('Замер времени для list comprehension: ', timeit("func_2(test[:])", globals=globals(), number=1000))

