print ('7. Вложенные циклы и генераторы')
#Общий синтаксис: [expression for x in iterator for y in x].
print ('\tНапример, создадим словарь, используя кортежи координат как ключи, заполнив для начала его значения нулями.')
rows = 1, 2, 3
cols = 'a', 'b'
my_dict = {(col, row): 0 for row in rows for col in cols}
print(my_dict)


print ('\n\tТоже можно сделать и с дополнительными условиями-фильтрами в каждом цикле:')
rows = 1, 2, 3, -4, -5
cols = 'a', 'b', 'abc'
# Для наглядности разнесем на несколько строк
my_dict = {
    (col, row): 0  # каждый элемент состоит из ключа-кортежа и нулевого знаечния
    for row in rows if row > 0   # Только положительные значения
    for col in cols if len(col) == 1  # Только односимвольные
    }
print(my_dict)

print ('\n7.1.2 Вложенные циклы for где внутренний цикл идет по результату внешнего цикла')
matrix = [[0, 1, 2, 3],
          [10, 11, 12, 13],
          [20, 21, 22, 23]]

# Решение с помощью генератора списка:
flattened = [n for row in matrix for n in row]
print(flattened)    # [0, 1, 2, 3, 10, 11, 12, 13, 20, 21, 22, 23]

import itertools
flattened = list(itertools.chain.from_iterable(matrix))  # от @iMrDron
# Данный подходнамного быстрее генератора списков
# и рекомендован к использованию для подобных задач.