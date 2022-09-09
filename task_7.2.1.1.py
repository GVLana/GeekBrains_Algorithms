"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


# Сортировка Шелла


def shellSort(lst_obj):
    n = len(lst_obj)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = lst_obj[i]
            j = i
            while j >= interval and lst_obj[j - interval] > temp:
                lst_obj[j] = lst_obj[j - interval]
                j -= interval
            lst_obj[j] = temp
        interval //= 2
    return lst_obj

m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
copy_orig_list = orig_list[:]
shellSort(copy_orig_list)
print(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')
print(timeit("shellSort(orig_list[:])", globals=globals(), number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
copy_orig_list = orig_list[:]
shellSort(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')

print(timeit("shellSort(orig_list[:])", globals=globals(), number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

copy_orig_list = orig_list[:]
shellSort(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')

print(timeit("shellSort(orig_list[:])", globals=globals(), number=100))