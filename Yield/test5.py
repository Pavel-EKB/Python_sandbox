def testGen():
    x = 2
    print('Первый yield')
    yield x

    x *= 1
    print('Второй yield')
    yield x

    x *= 1
    print('Последний yield')
    yield x

# Вызов генератора
iter = testGen()

# Вызов первого yield
next(iter)

# Вызов второго yield
next(iter)

# Вызов последнего yield
next(iter)