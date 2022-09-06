
# Задание 1 из урока 3:
# a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)


from memory_profiler import profile
from json import loads, dumps
from pympler import asizeof


# первоначальное решение задачи:

n = 100000

@profile
def fill_dict(num, res={}):
    for i in range(num):
        res[i] = i

res_dict = {}
fill_dict(n, res_dict)

# оптимизированное решение:

# генерация словаря и его сжатие с целью экономии памяти компьютера
new_dict = {i: i for i in range(n)}
dumped_dict = dumps(new_dict)
out_dict = loads(dumped_dict)

print('Размер первоначального словаря: ', asizeof.asizeof(res_dict))
print('Размер json: ', asizeof.asizeof(dumped_dict))