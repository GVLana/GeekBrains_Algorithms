"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

# вар 1 Сложность алгоритма O(N^2)
def search_min_1(my_list):
    for i in range(len(my_list)):                                    # O(N)
        for j in range(1, len(my_list)):                             # O(N)
            if my_list[j] < my_list[i]:                              # O(1)
                my_list[j], my_list[i] = my_list[i], my_list[j]      # O(1)
        return my_list[0]                                            # O(1)

print(search_min_1(my_list=[10,1,-7,9,-5]))


вар 2 Сложность алгоритма O(N)
def search_min_2(my_list):
    while len(my_list) > 1:                                         # O(N)
        if my_list[-1] >= my_list[-2]:                              # O(1)
            my_list.pop()                                           # O(1)
        else:
            my_list[-2], my_list[-1] = my_list[-1], my_list[-2]     # O(1)

    return my_list[0]                                               # O(1)

print(search_min_2(my_list=[10,1,8,9,-5]))