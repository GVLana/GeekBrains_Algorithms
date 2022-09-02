"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
import random
from collections import deque
from timeit import timeit

# append, pop, extend
my_list = [random.randint(0, 20) for i in range(1000)] #односторонняя очередь
my_deque = deque([random.randint(0, 20) for el in range(1000)]) #двусторонняя очередь
print(my_list)
print(my_deque)

extend_list = [65, 75, 89]

def list_append():
    while len(my_list) < 2000:
        i = random.randint(20, 30)
        my_list.append(i)
    return my_list

print(list_append())


def deque_append():
    while len(my_deque) < 2000:
        i = random.randint(20, 30)
        my_deque.append(i)
    return my_deque

print(deque_append())

def list_pop():
    while my_list:
        my_list.pop()
        if len(my_list) % 300 == 0:
            return my_list

print(list_pop())

def deque_pop():
    while my_deque:
        my_deque.pop()
        if len(my_deque) % 300 == 0:
            return my_deque

print(deque_pop())


def list_extend():
    for i in extend_list:
        my_list.extend([i])
    return my_list

print(list_extend())


def deque_extend():
    for i in extend_list:
        my_deque.extend([i])
    return my_deque

print(deque_extend())

print(my_list)
print(my_deque)
print(len(my_list))
print(len(my_deque))

print("Замер времени для list_append ", timeit("list_append()", globals=globals()))
print("Замер времени для deque_append", timeit("deque_append()", globals=globals()))
print("Замер времени для list_pop", timeit("list_pop()", globals=globals()))
print("Замер времени для deque_pop", timeit("deque_pop()", globals=globals()))
# print("Замер времени для list_extend", timeit("list_extend()", globals=globals()))
print("Замер времени для deque_extend", timeit("deque_extend()", globals=globals()))

# Выводы: разница в замерах времени для deque и list мала, при этом deque работает чуть быстрее.
# Возможно на более больших данных эта разница будет критична

# appendleft, popleft, extendleft
my_list = [random.randint(0, 20) for i in range(1000)] #односторонняя очередь
my_deque = deque([random.randint(0, 20) for el in range(1000)]) #двусторонняя очередь
print(my_list)
print(my_deque)

ext_list = [65, 75, 89]


def list_appendleft():
    while len(my_list) < 2000:
        i = random.randint(20, 30)
        my_list.insert(0, i)
    return my_list


print(list_appendleft())


def deque_appendleft():
    while len(my_deque) < 115:
        i = random.randint(20, 30)
        my_deque.appendleft(i)
    return my_deque

print(deque_appendleft())


def list_popleft():
    while my_list:
        my_list.pop(0)
        if len(my_list) % 300 == 0:
            return my_list


print(list_popleft())

def deque_popleft():
    while my_deque:
        my_deque.popleft()
        if len(my_deque) % 30 == 0:
            return my_deque

print(deque_popleft())


def list_extendleft():
    for i in ext_list:
        my_list.insert(0, i)
    return my_list

print(list_extendleft())


def deque_extendleft():
    for i in ext_list:
        my_deque.extendleft([i])
    return my_deque


print(deque_extendleft())

print("Замер времени для list_appendleft ", timeit("list_appendleft()", globals=globals()))
print("Замер времени для deque_appendleft ", timeit("deque_appendleft()", globals=globals()))
print("Замер времени для list_popleft ", timeit("list_popleft()", globals=globals()))
print("Замер времени для deque_popleft ", timeit("deque_popleft()", globals=globals()))
# print("Замер времени для list_extendleft ", timeit("list_extendleft()", globals=globals()))
print("Замер времени для deque_extendleft ", timeit("deque_extendleft()", globals=globals()))

# Выводы: операции appendleft и popleft и соответсвующие им операции списка близки по времени выполнения.
# Операция extendleft значительно превосходит соответсвующую операцию списка.

# сравнить операции получения элемента

my_list = [random.randint(0, 20) for j in range(1000)] #односторонняя очередь
my_deque = deque([random.randint(0, 20) for elem in range(1000)]) #двусторонняя очередь
print(my_list)
print(my_deque)

def get_el_list():
    i = random.randint(10, 50)
    if i in my_list:
        return my_list[i]
    return f'There is no such numer like {i}'

def get_el_deque():
    i = random.randint(10, 50)
    if i in my_deque:
        return my_deque[i]
    return f'There is no such numer like {i}'


print(get_el_list())
print(get_el_deque())

print("Замер времени для get_el_list ", timeit("get_el_list()", globals=globals(), number=1000))
print("Замер времени для get_el_deque ", timeit("get_el_deque()", globals=globals(), number=1000))

# Получение элемента по индексу в list производится быстрее, чем в deque.