# Код Python для демонстрации
# удаление элемента в списке
# использование списка понимания



test_list1 = [1, 3, 4, 6, 3]

test_list2 = [1, 4, 5, 4, 5]


# Печать начального списка

print ("The list before element removal is : "

                            + str(test_list2))




# использование списка понимания
# удалить элемент списка 4

test_list2 = [x for x in test_list2 if x != 4]


# Печать списка после удаления

print ("The list after element removal is : "

                           + str(test_list2))