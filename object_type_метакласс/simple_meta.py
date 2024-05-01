class MyMeta(type):
    def __new__(cls, name, bases, namespace):
        # cls - MyMeta
        # name - имя определяемого класса (MyClass в этом примере)
        # bases - базовые классы для построенного класса
        # namespace - словарь определенных в класса методов и полей
        # в нашем случае - {'x': 3}
        # super().__new__ просто возвращает новый класс
        return super().__new__(cls, name, bases, namespace)
class MyClass(metaclass=MyMeta):
    x = 3