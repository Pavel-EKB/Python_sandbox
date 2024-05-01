dict1 = {'a': ['qw', 'we', 'cd'], 'b': ['a1', 'a2', 'a3']}
print (dict1)
print (dict1.items())
print (dict1.keys())
print (dict1.values())
print (dict1.get('a'))
print (dict1['a'])
print (dict1['a'][1])


incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
def by_value(item):
    print (item)
    return item[1]

for k, v in sorted(incomes.items(), key=by_value):
    print(k, '->', v)
