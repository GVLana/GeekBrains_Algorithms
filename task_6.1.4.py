# Задание 4 Урока 4:
# Приведены два алгоритма. В них определяется число,
# которое встречается в массиве чаще всего.


from random import randint
from memory_profiler import profile
from numpy import array, argmax, bincount
from pympler import asizeof


my_list = [randint(0, 10) for el in range(30000)]

# один из вариантов первоначального решения
@profile
def func_2():
    new_array = []
    for el in my_list:
        count2 = my_list.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = my_list[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'



print(func_2())


# оптимизация процесса с помощью библиотеки numpy разница в отсутсвии затрат памяти на строку new_array.append(count2):
@profile
def func_5():
    res = bincount(array(my_list))
    return f'Чаще всего встречается число {argmax(res)}, ' \
           f'оно появилось в массиве {max(res)} раз(а)'

print(func_5())


# оптимизация генерации списка и вычислений из него:

new_list = array([randint(0, 10) for el in range(30000)])

@profile
def func_6():
    res = bincount(new_list)
    return f'Чаще всего встречается число {argmax(res)}, ' \
           f'оно появилось в массиве {max(res)} раз(а)'

print(func_6())

print('Размер первоначального спсика: ', asizeof.asizeof(my_list))
print('Размер нового списка: ', asizeof.asizeof(new_list))

