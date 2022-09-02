"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import string
from time import time

def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f'Function execution time {func.__name__} is {end - start}')
        return res

    return timer

# пункт а: заполнение списка и словаря

n = 100000

@time_decorator
def fill_list(num, res=[]):                 # O(1)
    for i in range(num):
        res.append(i)

res_list = []
fill_list(n, res_list)


@time_decorator
def fill_dict(num, res={}):                # O(1)
    for i in range(num):
        res[i] = i

res_dict = {}
fill_dict(n, res_dict)


# Аналитика: по сложности эти две функции одинаковы О(1). Время заполнения списка путем добавления элемента в конец - меньше,
# чем время заполнения словаря.


@time_decorator
def insert_list(num, res=[]):                 # O(n)
    for i in range(num):
        res.insert(0, i)

insert_list(n)

# Аналитика: Заполнени спсика через insrt имеет сложность О(n). Время заполнения словаря меньше,
# чем время заполнения спсика методом добавления элемента в начало списка, тк каждый раз элементы находящиеся в списке переиндексируются.


# пункт b: получение элемента списка и словаря
@time_decorator
def get_list(res):                                          #O(1)
    for i in range(int(n/100), int(n/10)):
        res[i] = 'I'

get_list(res_list)

@time_decorator
def get_dict(res):                                          #O(1)
    for i in range(int(n/100), int(n/10)):
        res[i] = 'I'

get_dict(res_dict)

# Аналитика: Обращение к элементу списка по индексу имеет такую же сложность, что обращение к значению словаря по ключу.

# пункт c: удаление элемента списка и словаря

@time_decorator
def pop_from_list(res):                                   #O(1)
    for i in range(len(res)):
        res.pop()

pop_from_list(res_list)

@time_decorator
def pop_i_from_list(res):                                 #O(n)
    for i in range(len(res)):
        res.pop(i)

pop_i_from_list(res_list)

@time_decorator
def pop_i_from_dict(res):                                #O(1)
    for i in range(n):
        res.pop(i)

pop_i_from_dict(res_dict)

# Аналитика: В случае, если методу pop() передается значение, то скорость этого метода падает и его сложность превращается в O(n).
# Словарь в данном случае работает намного быстрее.