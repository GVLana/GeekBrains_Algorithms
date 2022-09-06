# Задание 3 Урок 4:
# Приведен код, формирующий из введенного числа
# обратное по порядку входящих в него
# цифр и вывести на экран.


from memory_profiler import profile, memory_usage



# при применении profile к рекурсии будет выводится таблица подсчета памяти для каждого вызова рекурсии.
# Чтобы этого избежать, можно обернуть рекурсию в функцию

# первоначальный вариант:

# @profile
# def vice_versa(num, check=0, res=''):
#     if num == 0:
#         print('The reverse number is: ')
#         return res
#     else:
#         check = num % 10
#         num = num // 10
#         res = res + str(check)
#         return vice_versa(num, check, res)
#
# try:
#     user_input = int(input('Enter a number: '))
#     print(f'{vice_versa(user_input)}')
# except ValueError:
#     print('You enter a string not a number. Try again.')
#

#оптимизированнный вариант

@profile
def wrapper(n):
    def vice_versa(num, check=0, res=''):
        if num == 0:
            print('The reverse number is: ')
            return res
        else:
            check = num % 10
            num = num // 10
            res = res + str(check)
            return vice_versa(num, check, res)
    return vice_versa(n)

try:
    user_input = int(input('Enter a number: '))
    print(f'{wrapper(user_input)}')
except ValueError:
    print('You enter a string not a number. Try again.')



