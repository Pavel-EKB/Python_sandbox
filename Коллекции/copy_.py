#.copy() — метод возвращает неглубокую (не рекурсивную)
#копию коллекции (список, словарь, оба типа множества)
my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)  # True - коллекции равны - содержат одинаковые значения
print(my_set_2 is my_set)  # False - коллекции не идентичны - это разные объекты с разными id

import copy
print(copy.__file__)
my_set_2 = copy.deepcopy(my_set)
my_set.add(4)
print(my_set_2)
print (my_set)