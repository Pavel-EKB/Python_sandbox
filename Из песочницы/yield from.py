def generator_range(first, last):
    for i in xrange(first, last):
        yield i

def generator_range_1(first, last):
    yield from range(first, last)

f = generator_range_1(1, 4)
for i in f:
    print (i)