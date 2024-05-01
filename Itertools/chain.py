from itertools import chain

numbers = list(range(5))
cmd = ['ls', '/some/dir']

my_list = list(chain(['foo', 'bar'], cmd, numbers))

print(my_list)

numbers = list(range(5))
cmd = ['ls', '/some/dir']

data = list(chain.from_iterable([cmd, numbers]))
print(data)

print (cmd + numbers)