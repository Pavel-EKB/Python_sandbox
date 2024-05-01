def decor (items):
    def newfunc (fn):
        print ('Repeat')
        for i in range (items-1):
            fn()
        return fn
    return newfunc


@decor(items = 4)
def MyFunc():
    print('Test')

MyFunc()

#-------------------------------------------------------
def set_unit(unit):
    """Регистрирует юнит для переданной функции"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit

import math

@set_unit("см^3")
def volume(radius, height):
    return math.pi * radius**2 * height

print (volume(3, 5))