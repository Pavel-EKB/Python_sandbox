from operator import itemgetter

lst1 = (8, 1, 2, 3, 0, 4, 5, 5, 6, 7, 9, 9, 9)
lst2 = (1, 8, 7, 6, 9, 5, 4, 4, 3, 2, 0, 0, 0)
lst3 = (1, 5, 4, 6, 9, 5, 4, 4, 3, 2, 0, 0, 0)

def Test_key(lst):
    print(lst[0], '-', lst[1][0], '-', lst[1][1])
#   return lst[1][0] #сортируем по lst2
    return lst[0]    #сотрируем по lst1

zip_lst = zip(lst1, lst2, lst3)
print (list (zip_lst))

result = sorted({k: (v, p) for k, v, p in zip(lst1, lst2, lst3)}.items(),
        key=Test_key, reverse=True)

print (list (result))
lst1 = ([x for x, _ in result])
lst2 = ([x for _, x in result])

lst3 = ([x for x, _ in lst2])
lst4 = ([x for _, x in lst2])

print (lst1)
print (lst3)
print (lst4)