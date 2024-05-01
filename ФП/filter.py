#Для варианта с  функцией filter:

a = filter(lambda x: x >= 0, [-1, 1, -2, 2, 0])
print (list(a))
#аналог будет выглядеть так:

b = (v for v in [-1, 1, -2, 2, 0] if v > 0)
print (list(b))