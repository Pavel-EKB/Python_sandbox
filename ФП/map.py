a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x**2, a))
print (b)

def fun(x):
        if x % 2 == 0:
            return 0
        else:
            return x*2
c = list(map(fun, a))
print(c)

#Замена map
d = [x*3 for x in (a)]
print (d)


f = [x*2 for x in [a]]
print (f)