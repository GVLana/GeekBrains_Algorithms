"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""

from random import randint
from timeit import timeit
from statistics import median

def find_median(orig_list):
    return median(orig_list[:])


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(f'Median is {find_median(orig_list[:])}')
print(timeit("find_median(orig_list[:])", globals=globals(), number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(f'Median is {find_median(orig_list[:])}')
print(timeit("find_median(orig_list[:])", globals=globals(), number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

print(f'Median is {find_median(orig_list[:])}')
print(timeit("find_median(orig_list[:])", globals=globals(), number=100))

# самый быстрый способ поиска медианы - втроенная функция библиотеки statistic,
# затем алгоритм сортировки Шелл,
# на третьем месте  - алгоритм сортировки кучей,
# на последнем месте - без сортировки
