class Meter(object):
    '''Дескриптор для метра.'''
    '''Передаем через self'''

    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    '''Дескриптор для фута.'''

    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    '''Класс, описывающий расстояние, содержит два дескриптора для футов и
    метров.'''
    meter = Meter()
    foot = Foot()

test = Distance()
print (test.foot)
print (test.meter)
test.meter = 2.0
print (test.foot)
print (test.meter)
test.foot = 3.2808
print (test.foot)
print (test.meter)
test2 = Distance() #Возвращает то же значение, что и test
print (test2.foot)
print (test2.meter)