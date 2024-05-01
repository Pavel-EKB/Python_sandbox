from itertools import islice

iterator = islice('123456', 4)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4

#print(next(iterator)) # ошибка!

print ('\n')
from itertools import islice
from itertools import count

for i in islice(count(), 3, 15):
    print(i)