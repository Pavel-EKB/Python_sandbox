prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices[price] < 0.4

#filter() — это еще одна встроенная функция, которая фильтрует последовательность итерируемого объекта.
low_price = list(filter(has_low_price, prices.keys()))
print (low_price)

low_price1 = list(filter(lambda x: (prices[x] < 0.4), prices))
print (low_price1)

#map() — это встроенная функция Python, принимающая в качестве аргумента функцию и последовательность. Она работает так, что применяет переданную функцию к каждому элементу.
price_evens = map(lambda n: n, filter(lambda n: prices[n] < 0.4, prices))
print(list(price_evens))

low_price2 = list(k for k, v in prices.items() if v < 0.4)
print (low_price2)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_b = [x if x < 0 else x**2 for x in list_a]
# Если x-отрицательное - берем x, в остальных случаях - берем квадрат x
print(list_b)   # [-2, -1, 0, 1, 4, 9, 16, 25]

low_price3 = list(k if v < 0.4 else None for k, v in prices.items() )
print (low_price3)

squared_evens = map(lambda n: n, filter(lambda n: prices[n] < 0.4, prices))
print(list(squared_evens))