col = 'abcdefg'
print(col[:])       # abcdefg
print(col[::-1])    # gfedcba
print(col[::2])     # aceg
print(col[1::2])    # bdf
print(col[:1])      # a
print(col[-1:])     # g
print(col[3:4])     # d
print(col[-3:])     # efg
print(col[-3:1:-1]) # edc
print(col[2:5])     # cde

print ('\nСортировка строки')
print (sorted(col))
print ('\n')
my_list = [1, 2, 3, 4, 5, 6, 7]
EVEN = slice(1, None, 2)
print(my_list[EVEN])     # [2, 4, 6]

print ('\n')
my_list = [1, 2, 3, 4, 5]
print (my_list)
my_list[1:3] = [20, 30]
print(my_list)          # [1, 20, 30, 4, 5]
my_list[1:3] = [0]      # нет проблем заменить два элемента на один
print(my_list)          # [1, 0, 4, 5]
my_list[2:] = [40, 50, 60]   # или два элемента на три
print(my_list)               # [1, 0, 40, 50, 60]

my_list = [1, 2, 3, 4, 5]
my_list[:2] = []    # или del my_list[:2]
print(my_list)      # [3, 4, 5]