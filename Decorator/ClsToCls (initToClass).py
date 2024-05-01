class DecoratorArgs:
    def __init__(self, name):
        print('> Декоратор с аргументами __init__:', name)
        self.name = name

    def __call__(self, func):
        def wrapper(a, b):
            print('>>> до обернутой функции')
            func(a, b)
            print('>>> после обернутой функции')
        return wrapper

@DecoratorArgs("teste")
class MyClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print ('OK')

print('>> старт')
val = MyClass(3, 4)
print('>> конец')