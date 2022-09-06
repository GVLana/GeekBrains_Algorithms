
# Задание 2 Урок 2:	Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).



from random import getrandbits
from memory_profiler import profile

# первоначальный вариант

@profile
def wrapper(n):
    def even_odd(num, e_count=0, odd_count=0):
        if num == 0:
            print("Количество четных и нечетных цифр в числе равно: ")
            return e_count, odd_count
        else:
            check = num % 10
            num = num // 10
            if check % 2 == 0:
                e_count += 1
            else:
                odd_count += 1
            return even_odd(num, e_count, odd_count)
    return even_odd(n)

number = getrandbits(512)


print(f'{wrapper(number)}')


# замена рекурсии на цикл, тк он быстрее и не требует дополнительной памяти
@profile
def even_odd_2(num, e_count=0, odd_count=0):

    while num != 0:
        check = num % 10
        num = num // 10
        if check % 2 == 0:
            e_count += 1
        else:
            odd_count += 1
    print('Количество четных и нечетных числе в even_odd_2 равно: ')
    return e_count, odd_count



print(f'{even_odd_2(number)}')
