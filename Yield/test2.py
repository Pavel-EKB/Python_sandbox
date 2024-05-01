# Создаем список
alist = [4, 16, 64, 256]

# Вычислим квадратный корень, используя генерацию списка
out = [a**(1/2) for a in alist]
print(out)

# Используем выражение генератора, чтобы вычислить квадратный корень
out = (a**(1/2) for a in alist)
print(out)
print(next(out))
print(next(out))
print(next(out))
print(next(out))
print(next(out)) #выведет ошибку