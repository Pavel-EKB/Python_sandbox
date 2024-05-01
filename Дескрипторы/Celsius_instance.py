class Celsius:
    '''Передаем через instance'''
    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5


class Temperature:

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(212)
print(t.celsius)
print(t.fahrenheit)

print ('For t: celsius, fahrenheit')
t.celsius = 3
print(t.celsius)
print(t.fahrenheit)
t2 = Temperature(212)
print ('For t2: celsius, fahrenheit')
print(t2.celsius)
print(t2.fahrenheit)