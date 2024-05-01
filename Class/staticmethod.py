class Myclass():
    @staticmethod
    def staticmethod():
        print('static method called')

Myclass.staticmethod()
#вызов метода из экземпляра класса
my_obj = Myclass()
my_obj.staticmethod()

class Person():
    @staticmethod
    def is_adult(age):
        if age > 18:
            return True
        else:
            return False

print (Person.is_adult(23))