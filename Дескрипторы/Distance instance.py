class Meter(object):
    '''Дескриптор для метра.'''
    '''Передаем через instance'''

    def __get__(self, instance, owner):
        return instance.value
    def __set__(self, instance, value):
        instance.value = float(value)

class Foot(object):
    '''Дескриптор для фута.'''

    def __get__(self, instance, owner):
        print (instance.__dict__)
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    '''Класс, описывающий расстояние, содержит два дескриптора для футов и
    метров.'''
    meter = Meter()
    foot = Foot()

    def __init__(self, value=0.0):
        self.value = float(value)

test = Distance()
print (test.meter)
print (test.foot)

test.meter = 2.0
print (test.meter)
print (test.foot)

test.foot = 3.2808
print (test.meter)
print (test.foot)

print ('test2 = Distance()')
test2 = Distance()
print (test2.meter)
print (test2.foot)