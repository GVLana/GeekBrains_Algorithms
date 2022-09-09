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


# Сортировка кучей


def heapify(lst_obj, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and lst_obj[left_child] > lst_obj[largest]:
        largest = left_child

    if right_child < heap_size and lst_obj[right_child] > lst_obj[largest]:
        largest = right_child

    if largest != root_index:
        lst_obj[root_index], lst_obj[largest] = lst_obj[largest], lst_obj[root_index]
        heapify(lst_obj, heap_size, largest)

def heap_sort(lst_obj):
    n = len(lst_obj)

    for i in range(n, -1, -1):
        heapify(lst_obj, n, i)

    for i in range(n - 1, 0, -1):
        lst_obj[i], lst_obj[0] = lst_obj[0], lst_obj[i]
        heapify(lst_obj, i, 0)

m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
copy_orig_list = orig_list[:]
heap_sort(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')
print(timeit("heap_sort(orig_list[:])", globals=globals(), number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
copy_orig_list = orig_list[:]
heap_sort(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')

print(timeit("heap_sort(orig_list[:])", globals=globals(), number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

copy_orig_list = orig_list[:]
heap_sort(copy_orig_list)
print(f'Median is {copy_orig_list[len(copy_orig_list )//2]}')

print(timeit("heap_sort(orig_list[:])", globals=globals(), number=100))

