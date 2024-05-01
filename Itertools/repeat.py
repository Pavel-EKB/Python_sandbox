from itertools import repeat

iterator = repeat('test', 5)

print(next(iterator)) # test
print(next(iterator)) # test
print(next(iterator)) # test
print(next(iterator)) # test
print(next(iterator)) # test

# В 6й раз будет ошибка...
# print(next(iterator))