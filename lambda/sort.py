# Сортировка словаря
d = {'a': 10, 'b': 15, 'c': 4}
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
print(list_d)
# Вывод
#[('c', 4), ('a', 10), ('b', 15)]