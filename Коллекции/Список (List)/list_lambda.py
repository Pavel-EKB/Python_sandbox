# Код Python для демонстрации
# удаление элемента в списке
# используя filter () + лямбда-функция



test_list1 = [1, 3, 4, 6, 3]

test_list2 = [1, 4, 5, 4, 5]


# Печать начального списка

print ("The list before element removal is : "

                            + str(test_list1))


# используя filter () + лямбда-функция
# удалить элемент списка 3

test_list1 = list(filter(lambda x: x != 3, test_list1))


# Печать списка после удаления

print ("The list after element removal is : "

                           + str(test_list1))