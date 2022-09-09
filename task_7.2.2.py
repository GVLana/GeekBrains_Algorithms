
"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def find_median_without_sorting(lst_obj):
        res = 0
        for el in lst_obj:
            count = 0
            for x in lst_obj:
                if x < el:
                    count += 1
            if count == len(lst_obj) // 2:
                res = el
                break
        return res


m = 10
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

copy_orig_list = orig_list[:]

print(f'Median is {find_median_without_sorting(copy_orig_list)}')
print(timeit("find_median_without_sorting(orig_list[:])", globals=globals(), number=100))

m = 100
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
copy_orig_list = orig_list[:]

print(f'Median is {find_median_without_sorting(copy_orig_list)}')
print(timeit("find_median_without_sorting(orig_list[:])", globals=globals(), number=100))

m = 1000
orig_list = [randint(0, 100) for i in range(2 * m + 1)]

copy_orig_list = orig_list[:]

print(f'Median is {find_median_without_sorting(copy_orig_list)}')
print(timeit("find_median_without_sorting(orig_list[:])", globals=globals(), number=100))

