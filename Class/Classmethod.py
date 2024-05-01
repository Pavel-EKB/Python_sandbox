class MyClass:
    @classmethod
    def classmethod(cls):
        print('Class method called')

MyClass.classmethod()

#-------------------------------------------
class MyClass():

    TOTAL_OBJECTS=0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS+1

    @classmethod
    def total_objects(cls):
        print("Total objects: ",cls.TOTAL_OBJECTS)
# Создаем объекты родительского класса
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
# Вызываем classmethod
MyClass.total_objects()

# Создаем дочерний класс
class ChildClass(MyClass):
    TOTAL_OBJECTS=0
    pass
ChildClass.total_objects()