import random
from random import randint
n=10
mas = [randint(1,10) for i in range(n)]
for i in range(n):
                print(mas[i],sep="")


for i in range(n-1):
                for j in range(n-2, i-1 ,-1):
                    if mas[j+1] < mas[j]:
                        mas[j], mas[j+1] = mas[j+1], mas[j]
print("   ")
for i in range(n):
                print(mas[i],sep="")


