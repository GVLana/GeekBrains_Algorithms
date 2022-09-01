"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

dataBase = {'Pulaner': 155000, 'Kozel': 136850, 'Boonville': 95300, 'Bulmers': 65140, "Ballantine": 195000}
print(list(dataBase.values()))

# вар 1 Сложность алгоритма O(N)
def max_profit(db):
    output = []                                                             # O(1)
    values = list(db.values())                                              # O(N)
    m = 0                                                                   # O(1)
    while len(output) < 3:                                                  # O(N)
        for i in range(len(values)):                                        # O(N)
            if m < values[i]:                                               # O(1)
                m = values[i]                                               # O(1)
        output.append(m)                                                    # O(1)
        values.remove(m)                                                    # O(N)
        m = 0                                                               # O(1)
    return [k for k, v in db.items() for item in output if v == item]       # O(N)

print(max_profit(dataBase))

# вар 2 Сложность алгоритма O(N^2)
def max_profit_2(db):
    sorted_values = sorted(db.values())                                     # O(N log N)
    sorted_db = []                                                          # O(1)
    for v in sorted_values:                                                 # O(N)
        for k in db.keys():                                                 # O(N)
            if db[k] == v:                                                  # O(1)
                sorted_db.append(k)                                         # O(1)
                break
    return sorted_db[-3:]                                                 # O(len(sorted_db))

print(max_profit_2(dataBase))

# вар 3 Сложность алгоритма O(N log N)
def max_profit_3(db):
    return list(dict(sorted(db.items(), key=lambda x: x[1], reverse=True)))[:3]

print(max_profit_3(dataBase))

# Наиболее оптимальные варианты: 1 и 3. У них сложность меньше. При этом вариант 3 более прост для понимания, а в варианте 1 - много действий.