def simple_generator():
   tmp = 0
   while True:
       yield tmp
       tmp += 1

sg = simple_generator()
print (next(sg))
print (next(sg))
print (next(sg))
del sg

#Итераторы позволяют строить ленивые вычисления. Например, функции для работы с последовательностями map(), filter(), range(), zip() и т.п. возвращают итератор

print('Next generator')
a = [1, 2, 3]
a_sq = map(lambda x: x**2, a)

print (next(a_sq))
print (next(a_sq))
print (next(a_sq))

print (list(a_sq))