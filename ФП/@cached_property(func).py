#Декоратор, который позволяет создавать свойства класса с поддержкой кэширования.

import functools
class DataProc:
   def __init__(self, data_set):
      self._data_set = data_set

   @functools.cached_property
   def mean(self):
      return sum(self._data_set) / len(self._data_set)

d = DataProc([1,2,3,4,5])
print(d.mean)