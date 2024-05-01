a = [3, 1, 2]
b = ['a', 'b', 'c']
c = ['z', 'x', 'y']

#соединим два списка специальной функцией zip
x = zip(a,b,c)
print (list(zip(a,b,c)))

#отсортируем, взяв первый элемент каждого списка как ключ
xs = sorted(x, reverse=True)

#и последний шаг - извлечем
a1 = [x[0] for x in xs]
b1 = [x[1] for x in xs]
c1 = [x[2] for x in xs]

print (a1)
print (b1)
print (c1)