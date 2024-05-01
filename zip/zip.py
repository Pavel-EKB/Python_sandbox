a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
for i, j in zip(a, b):
    print (i, j)

print ('\nNext example-списки разной длины-----------')

from itertools import zip_longest
a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
c = [1.1, 1.2]
for i in zip_longest(a,b,c):
    print(i)

print ('\nNext example-"0" вместо None--------')
from itertools import zip_longest
a = [10, 20, 30, 40]
b = ['a', 'b', 'c', 'd', 'e']
c = [1.1, 1.2]
for i in zip_longest(a,b,c, fillvalue=0):
    print(i)

print ('\nNext example-list--------')
a = [10, 20, 30, 40]
c = [1.1, 1.2, 1.3, 1.4]
ac = zip(a, c)
ac = list(ac)
print (ac)