

"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
from collections import Counter
from random import randint

array = [1, 3, 1, 3, 4, 5, 1]
# array = [randint(0, 10) for el in range(10)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


print(func_1())
print(func_2())

# Возможные варианты решения:

def func_3():
    count = Counter(array)
    result = max(count, key=count.get)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(func_3())

def func_4():
    result = max(array, key=array.count)
    return f'Чаще всего встречается число {result}, ' \
           f'оно появилось в массиве {array.count(result)} раз(а)'


print(func_4())


print('Замер времени для func_1: ', timeit("func_1()", globals=globals()))
print('Замер времени для func_2: ', timeit("func_2()", globals=globals()))
print('Замер времени для func_3: ', timeit("func_3()", globals=globals()))
print('Замер времени для func_4: ', timeit("func_4()", globals=globals()))

# Аналитика: Вне зависимости от размера array самым быстрым вариантом будет №4, тк не происходит никаких лишних действий.
# Вариант 3 хоть и использует стандартную библиотеку и встроенные функции будет самым медленным, тк сперва формирует словарь, а змтем оттуда выбирает нужные данные.
# Варианты 2 и 3 также занимают память компьютера, тк создают список/словарь.
