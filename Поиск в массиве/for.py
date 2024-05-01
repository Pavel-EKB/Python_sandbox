import random
from random import randint
n=10;x=5
mas = [randint(1,10) for i in range(n)]
print (mas)

nomer = 0
for i in range (n):
     if mas[i] == x:
        print ( "mas[", i, "]=", x, sep = "" )
        nomer = 1

if nomer == 0:
    print ( "Не нашли!" )