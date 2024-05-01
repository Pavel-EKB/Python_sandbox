multiply = lambda x,y,z: x * y + 1 if (x>20) else None
print (multiply(21, 2, 1))

#Лямбда-функция и filter
print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))

#или
print(list(map(lambda x: x, filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21]))))

#или
def even_fn(x):
  if x % 2 == 0:
    return True
  return False

print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))