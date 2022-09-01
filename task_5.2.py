"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

from collections import defaultdict


num_1 = int(input("Enter your first hexadecimal number: ").upper(), 16)
num_2 = int(input("Enter your second hexadecimal number: ").upper(), 16)

symbols = "".join([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])
d_dict = defaultdict(int)

# вариант defaultdict

count = 0
for key in symbols:
    d_dict[key] += count
    count += 1


def dec_to_hex(num):
    res = []
    while num:
        d = num % 16
        for k, v in d_dict.items():
            if v == d:
                res.append(k)
        num //= 16
    res.reverse()
    return res


print(f'Sum of two hexadecimal numbers: {dec_to_hex(num_1 + num_2)}')
print(f'Multiplication of two hexadecimal numbers: {dec_to_hex(num_1 * num_2)}')

# встроенная функция

print(f'Sum of two hexadecimal numbers: {list(hex(num_1 + num_2)[2:].upper())}')
print(f'Multiplication of two hexadecimal numbers: {list(hex(num_1 * num_2)[2:].upper())}')

