class E:
    def f(x):
        print(x)
    f = staticmethod(f)

#может быть вызвана либо из объекта, либо из класса
E.f(3)
E().f(3)