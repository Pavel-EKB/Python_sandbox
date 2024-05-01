from itertools import cycle

count = 0
for item in cycle('XYZ'):
    if count > 8:
        break
    print(item)
    count += 1

polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)

print(next(iterator)) # triangle
print(next(iterator)) # square
print(next(iterator)) # pentagon
print(next(iterator)) # rectangle
print(next(iterator)) # triangle
print(next(iterator)) # square