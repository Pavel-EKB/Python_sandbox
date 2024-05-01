numbers = range(10)
squared_evens = map(lambda n: n ** 2, filter(lambda n: n % 2 == 0, numbers))
print(list(squared_evens))