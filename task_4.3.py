"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit

e_num = 123456789

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# использование join:
def revers_4(enter_num):
    return "".join(reversed(str(enter_num)))



print('Замер времени для рекурсии: ', timeit(f'revers_1({e_num})', globals=globals()))

print('Замер времени для циклах: ', timeit(f'revers_2({e_num})', globals=globals()))

print('Замер времени для среза: ', timeit(f'revers_3({e_num})', globals=globals()))

print('Замер времени для join: ', timeit(f'revers_4({e_num})', globals=globals()))

# Рекурсия - является элегантым способом решения сложных задач, но не славится своей скоростью, часто уступая в ней циклам.
# Цикл работает хорошо, но внтури него (как и у рекурсии) происходят вычисления, на что требуется доп время.
# Встроенные функции (revers_4) адаптированы и работают достаточно быстро. Но в примере 4 использовано несколько встроенных функций. Они работают быстрее, чем цикл и рекурсия в данном примере.
# Срез - не производит никаких вычислений и является самым эффективным способом решения этой задачи.