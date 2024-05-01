class Celsius:
    '''Передаем через self'''
    def __init__(self, initial_f):
        self.fahrenheit = initial_f

    def __get__(self, instance, owner):
        print (instance, 'instance __dcit__:', instance.__dict__)
        return 5 * (self.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        self.fahrenheit = 32 + 9 * value / 5


class Temperature:

    celsius = Celsius(212)


t = Temperature()
#t.celsius = 0
print(t.celsius)
#print(t.fahrenheit)

t2 = Temperature()
t2.celsius = 3
t2.__dict__['celsius'] = 8
print ('t2__dict__:', t2.__dict__)
print ('For t: celsius, fahrenheit')
print(t.celsius)
#print(t.fahrenheit)
print ('For t2: celsius, fahrenheit')
print(t2.celsius)
#print(t2.fahrenheit)
print(t2.__dict__['celsius'])
#print(t2.fahrenheit)
print(t2.celsius)