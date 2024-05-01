# Код Python для демонстрации
# удаление элемента в списке
# используя метод pop ()



test_list1 = [1, 3, 4, 6, 3]


# Печать начального списка

print ("The list before element removal is : "

                            + str(test_list1))



rmv_element = 3


# используя pop ()
# удалить элемент списка 4

if rmv_element in test_list1:

    test_list1.pop(test_list1.index(rmv_element))


# Печать списка после удаления

print ("The list after element removal is : "

                           + str(test_list1))


# Добавлено Paras Jain (все возможно)