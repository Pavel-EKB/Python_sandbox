from operator import itemgetter

lst1 = (8, 1, 2, 3, 0, 4, 5, 5, 6, 7, 9, 9, 9)
lst2 = (1, 8, 7, 6, 9, 5, 4, 4, 3, 2, 0, 0, 0)
lst3 = (1, 8, 7, 6, 9, 5, 4, 4, 3, 2, 0, 0, 0)

zip_lst = zip(lst1, lst2, lst3)
print (list (zip_lst))

result = sorted({k: v for k, v, p in zip(lst1, lst2, lst3)}.items(),
        key=itemgetter(0), reverse=True)

print (list (result))
lst1 = ([x for x, _ in result])
lst2 = ([x for _, x in result])

print (lst1)
print (lst2)