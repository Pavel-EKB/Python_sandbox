class MyClass:
    @staticmethod
    def ex_static_method():
        print("static method")
    @classmethod
    def ex_class_method(cls):
        print("class method")
    def ex_method(self):
        print("method")

MyClass.ex_static_method()
MyClass.ex_class_method()
#Статический и классовый метод можно вызвать,
#не создавая экземпляр класса, для вызова ex_method() нужен объект
m = MyClass()
m.ex_method()