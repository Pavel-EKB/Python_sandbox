import random # подключение библиотеки
from random import randint
n=10; x=5
mas = [randint(1,10) for i in range(n)] # инициализируем массив

print (mas)
i=0
f=0
while i<n:
    if mas[i] ==x:
        print ( "mas[", i, "]=", x, sep = "" )
        f=1
    i+=1
if f==0:
    print ( "Не нашли!" )