# -*- coding: utf-8 -*-
'''Один из самых простых способов использования property, это использовать его в качестве декоратора метода. Это позволит вам превратить метод класса в атрибут класса'''

class Person(object):
    """"""
    def __init__(self, first_name, last_name):
        """Конструктор"""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """
        Возвращаем полное имя
        """
        return "%s %s" % (self.first_name, self.last_name)

person = Person("Mike", "Driscoll")

print(person.full_name) # Mike Driscoll
print(person.first_name) # Mike

#person.full_name = "Jackalope"

print ('--------------------------')

class Person_new():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def get_name (self):
        return "%s %s" % (self.f_name, self.l_name)

new_person = Person_new("Mickle", "Jackson")
print (new_person.get_name())
print (new_person.f_name)
