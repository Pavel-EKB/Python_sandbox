# Код Python для демонстрации
# удаление элемента в списке
# используя метод discard ()



test_list1 = [1, 3, 4, 6, 3]

test_list2 = [1, 4, 5, 4, 5]


# Печать начального списка

print ("The list before element removal is : "

                             + str(test_list1))


# используя discard () для удаления элемента списка 4

test_list1 = set(test_list1)

test_list1.discard(3)



test_list1 = list(test_list1)


# Печать списка после удаления
# удаляет элемент как отличный изначально

print ("The list after element removal is : "

                           + str(test_list1))