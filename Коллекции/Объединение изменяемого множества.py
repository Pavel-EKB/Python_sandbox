print('.difference_update()')

a = {'a', 'b'}
b = {     'b', 'c'}
a.difference_update(b)
print(a, b)         # {'a'} {'b', 'c'}
a = {'a', 'b'}
b = {     'b', 'c'}
b.difference_update(a)
print(a, b)         # {'a', 'b'} {'c'}

print('.intersection_update()')

a = {'a', 'b'}
b = {     'b', 'c'}
a.intersection_update(b)
print(a, b)         # {'b'} {'b', 'c'}

a = {'a', 'b'}
b = {     'b', 'c'}
b.intersection_update(a)
print(a, b)         # {'b', 'a'} {'b'}

print('.symmetric_difference_update()')

a = {'a', 'b'}
b = {     'b', 'c'}
a.symmetric_difference_update(b)
print(a, b)         # {'c', 'a'} {'c', 'b'}

a = {'a', 'b'}
b = {     'b', 'c'}
b.symmetric_difference_update(a)
print(a, b)         # {'a', 'b'} {'c', 'a'}