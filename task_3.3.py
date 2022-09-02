"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

from hashlib import sha256
# from itertools import combinations

s = input("Enter a string that has only letters: ").lower()


def hash_substrings(S):
    hash_set = set()
    my_set = set()
    n = len(S)
    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] != s:
                my_set.add(s[i:j])
                hash_set.add(sha256(s[i:j].encode()).hexdigest())
    print(f'Set of distinct substrings: {my_set}.')
    print(f'Hash-set of distinct substrings: {hash_set}.')
    return len(my_set)


print(hash_substrings(s))

