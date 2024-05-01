print ('.extend():')
a = [1, 2, 3]
b = [4, 5]
a.extend(b)    # a += b эквивалентно a.extend(b)
print(a, b)    # [1, 2, 3, 4, 5]  [4, 5]
print ('.append():')
a = [1, 2, 3]
b = [4, 5]
a.append(b)    # a += [b] эквивалентно a.append(b)
print(a, b)    # [1, 2, 3, [4, 5]]  [4, 5]