print ('через groupby, после сортировки----------------')
from itertools import groupby

x = ['a', 'a', 'a', 'f', 'h', 'k', 'k', 'a']
x = sorted(x) #без сортировки не работает
new_x = [el for el, _ in groupby(x)]

print(new_x)    # ['a', 'f', 'h', 'k']

print ('\nчерез set----------------')
l = [2, 1, 2, 3, 4, 5, 1, 5, 4, 3]
print (list(set(l)))

print ('\nУниверсальный способ:-----------')
def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n


print (f([1, 1, 2, 3, 3, [4, 5, 6]])) # [1, 2, 3, [4, 5, 6]]
print (f([[1, 2], [1, 2], 3, 4, 4, 'oops', 'oops'])) # [[1, 2], 3, 4, 'oops']

print('Сводная ---------------------------')
import itertools
x = 2, 2, 4, 3, 3, 1, 1, 2, 5, 4, 2, 1
print('data1:', x)


# простой спрособ - set, но теряется сортировка исходного списка
r = set(x)
print('set:', r)


# способ groupby подходит не совсем, тк уникальны только элементы идущие подряд
r = [a[0] for a in itertools.groupby(x)]
print('неверно groupby no sort:', r)

r = set(a[0] for a in itertools.groupby(x))
print('верно groupby no sort:', r)

# если список сначала отсортировать
r = [a[0] for a in itertools.groupby(sorted(x))]
print('groupby sort:', r)


# способ при котором не теряется сортировка исходного списка
def unique(obj: iter):
    args = []
    for a in obj:
        if a not in args:
            args.append(a)
            yield a

r = unique(x)
print('original sort unique:', *r)


# если список вложенный и заранее неизвесна степень вложенности
x = 2, (2, 4), [3], [3, [1, [1, 2, ([5],)], [4]], 2, 1]
print('\ndata2:', x)

def unpack(obj: iter):
    for o in obj:
        if isinstance(o, (list, tuple)):
            yield from unpack(o)
        else: yield o

r = unique(unpack(x))
print('unpack', *r)