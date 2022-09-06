# Задание 1 Урок 4:
# Приведен код, который позволяет сохранить в
# массиве индексы четных элементов другого массива
# Сделайте замеры времени выполнения кода с помощью модуля timeit
# Попробуйте оптимизировать код, чтобы снизить время выполнения


from memory_profiler import profile


# первоначальное решение и его оптимизация:

test = [i for i in range(100000)]

@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

func_1(test)


#list comprehension - тоже использует цикл for но выигрывает по скорости т.к. не вызывает метод append у списка
@profile
def func_2(nums):
    new_arr = [i for i, el in enumerate(nums) if el % 2 == 0]
    return new_arr

func_2(test)

# оптимизация решения с использованием filter / mem usage самая маленькая из трех вариантов
@profile
def func_3(lst):
    new_arr = filter(lambda x: x % 2 == 0, lst)
    return new_arr

func_3(test)