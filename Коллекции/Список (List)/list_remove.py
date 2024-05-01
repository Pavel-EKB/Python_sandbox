# Код Python для демонстрации
# удаление элемента в списке
# используя метод remove ()



test_list1 = [1, 3, 4, 6, 3]

test_list2 = [1, 4, 5, 4, 5]


# Печать начального списка

print ("The list before element removal is : "

                            + str(test_list1))


# используя remove () для удаления списка element3

test_list1.remove(3)


# Печать списка после удаления
# удалено только первое вхождение

print ("The list after element removal is : "

                           + str(test_list1))