
# Задание 1 из урока 3:
# a) заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)



from memory_profiler import profile
from pympler import asizeof
from numpy import array
from random import randint



# первоначальное решение задачи:

n = 100000

@profile
def fill_list(num, res=[]):
    for i in range(num):
        res.append(i)

res_list = []
fill_list(n, res_list)

# оптимизированное решение:

# генерация списка с использованием arrya позволяет создать список, занимающий меньше памяти

print('Размер первоначального спсика: ', asizeof.asizeof(res_list))
new_list = array([randint(0, 100) for _ in range(n)])
print('Размер нового списка: ', asizeof.asizeof(new_list))




