"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

ordict = OrderedDict()

ordict ["one"] = 1
ordict ["two"] = 2
ordict ["three"] = 3

print(ordict)


dict= {}

dict['a'] = 1
dict['b'] = 2
dict['c'] = 3

print(dict)

new_dict = {'a': 5, 'v' : 9}
new_ordict = OrderedDict()
new_ordict['three'] = 30
new_ordict['four'] = 4

print("Замер времени для dict_items", timeit("dict.items()", globals=globals()))
print("Замер времени для ordict_items ", timeit("ordict.items()", globals=globals()))

print("Замер времени для dict_get", timeit("dict.get('a')", globals=globals()))
print("Замер времени для ordict_get ", timeit("dict.get('one')", globals=globals()))

print("Замер времени для dict_revers", timeit("reversed(dict)", globals=globals()))
print("Замер времени для ordict_revers ", timeit("reversed(ordict)", globals=globals()))

print("Замер времени для dict_update", timeit("dict.update(new_dict)", globals=globals()))
print("Замер времени для ordict_update ", timeit("ordict.update(new_ordict)", globals=globals()))

# нет такого метода у словаря
print("Замер времени для ordict_sorted ", timeit("ordict.sorted_keys = lambda: sorted(ordict.keys())", globals=globals()))

# нет такого метода у словаря
print("Замер времени для ordict_move_to_end ", timeit("ordict.move_to_end('one')", globals=globals()))


# в Версиях Python 3.6+ словарь также сохраняет свой порядок, как и OrderedDict. OrderedDict - в случае, если подразумевается,
# что код будет использоваться и в более ранних версиях Python. Также OrderedDict имеет более сильный контроль за порядком, так там присутствует
# метод move_to_end(), а  у словаря более низкий контроль (требуется удаление и повторная вставка элементов).
# В целом OrderedDict уступает словарю по скорости и требует больше памяти.
# Думаю, что в основном следует использовать словарь.
# В случаях же если над данными в основном будет производиться сортировка или перемещение внутри словаря, то надо использовать OrderedDict.