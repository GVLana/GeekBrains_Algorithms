"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

from random import randint
from timeit import timeit

#первоначальный вариант с сортировкой по убыванию.
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort(orig_list[:])", globals=globals(), number=1000))

# доработанный вариант - break - в случае, если не происходит операции сортировки за проход, те достигли результата

def bubble_sort_opt(lst_obj):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                swap = True
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

print(timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

print(timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort_opt(orig_list[:])", globals=globals(), number=1000))

# Аналитика: При увеличении массива (с 10 до 1000) улучшение в скорости не происходит.
# Наоборот, при нескольких запусках показывало увеличение времени выполнения.
# Возможно это происходит потому, что при таком рандомном создании массива с широким диапазоном данных
# вероятность получения отсортированного массива за енсколько или один проход - мала.


# двойная оптимизация / все равно чуть больше времени требует, хотя внутренний цикл имеет больше ограничений для выполнения
def bubble_sort_opt_double(lst_obj):
    n = 0
    swap = True
    while swap:
        swap = False
        for i in range(len(lst_obj)-n-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                swap = True
        n += 1
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]

print(timeit("bubble_sort_opt_double(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

print(timeit("bubble_sort_opt_double(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort_opt_double(orig_list[:])", globals=globals(), number=1000))


# двойная оптимизация / все равно чуть больше времени требует, хотя внутренний цикл имеет больше ограничений для выполнения
def bubble_sort_opt_another(lst_obj):
    swap = False
    for i in range(len(lst_obj) - 1, 0, -1):
        for j in range(i):
            if lst_obj[j] > lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
                swap = True
        if swap:
            swap = False
        else:
            break
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]

print(timeit("bubble_sort_opt_another(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

print(timeit("bubble_sort_opt_another(orig_list[:])", globals=globals(), number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

print(timeit("bubble_sort_opt_another(orig_list[:])", globals=globals(), number=1000))
