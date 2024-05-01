class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

#Вызов из объекта
obj = MyClass()
print (obj.method())
# или
print (MyClass.method(obj))

print (obj.classmethod())

print (obj.staticmethod())

#Вызов из класса
print (MyClass.classmethod())

print (MyClass.staticmethod())

print (MyClass.method())