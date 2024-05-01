#map() определяется как map(function, iterable, …) и возвращает итератор,
#который применяет функцию к каждому элементу итерируемого.
print ('function-----------')
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))
new_prices = dict(map(discount, prices.items()))
print (new_prices)
#discount() возвращает кортеж в форме (key, value), где current_price[0]
#представляет ключ, а round(current_price [1] * 0.95, 2) представляет новое значение.
print ('\nlambda-----------')
elements_upper = dict(map(lambda x:(x.title(), round(prices[x] * 0.95, 2)),prices))
print (elements_upper)

print ('\nгенератор-----------')
new_price2 = {v.title():round(k *0.95, 2) for v, k in prices.items()}
print (new_price2)

print('\n')
gen_dict = (lambda x=3: dict([(y, y*y) for y in range(x)]))
print(gen_dict())

a,b=1,2
y = lambda :a+b
print (y())

elements_upper = list(map(lambda x:x.title(),prices))
print (elements_upper)

d = {'a': 1, 'b': 2}
values = map(lambda key: d[key]+1, d.keys())
print(list(values))

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
values1 = map(lambda key: prices[key]+1, prices.keys())
print(list(values1))


dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print (list(map(lambda x : x['name'], dict_a))) # Output: ['python', 'java']

print (list(map(lambda x : x['points']*10,  dict_a))) # Output: [100, 80]

print (list(map(lambda x : x['name'] == "python", dict_a))) # Output: [True, False]

#elements_upper = ['Hidrogen','Helium','Carbon']
#new_prices = dict(map(lambda x: x.title(), prices))
#print (new_prices)

lookup = {'A': 'aaa', 'B': 'bbb', 'C': 'ccc'}
keys = ['A', 'B', 'Z'] # Note 'Z' does not exist in dic
result = dict((lambda x: (x, lookup[x]) if x in lookup else (x, None))(key) for key in keys)
print (result)