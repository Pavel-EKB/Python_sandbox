dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
print (dict_abc.items())
print (dict_abc.keys())
print (dict_abc.values())
print (dict_abc.get('a'))
print (dict_abc['a'])


person = {'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna',
'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}

print(person['children'][-1])

print(person['pets']['cat'])

n_list = list(dict_abc.items())
print (n_list[1][0], '-', n_list[1][1])

key_list = list(dict_abc.keys())
print (key_list)

print (dict_abc[key_list[1]])