from itertools import tee

data = 'ABCDE'
iter1, iter2 = tee(data)

for item in iter1:
    print(item)

print('\n')
for item in iter2:
    print(item)