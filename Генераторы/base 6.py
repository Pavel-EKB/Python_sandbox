print ('6.1 Работа с enumerate()')
print ('\tздесь x — текущий элемент i — его порядковый номер, начиная с нуля')
list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
list_e = [x for i, x in enumerate(list_a, 1) if i % 3 == 0]
print(list_e)

first_ten_even = [(i, x) for i, x in enumerate(range(10)) if x % 2 == 0]
print(first_ten_even)

print ('\nИндексы считаются для всех обработанных элементов, без учета прошли они в дальнейшем условие или нет')
import itertools
first_ten = (itertools.islice((x for x in range(1000000000) if x % 2 == 0), 10))
print(list(first_ten))