from itertools import combinations

data = list(combinations('WXYZ', 2))
print(data)

print ('\n')

from itertools import combinations

for item in combinations('WXYZ', 2):
    print(''.join(item))