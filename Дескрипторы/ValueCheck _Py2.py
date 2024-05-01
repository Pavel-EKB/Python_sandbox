class NonNegative:
    def __init__(self, name): #для Python 2
        self.name = name  # (4)
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]  # (5)
    def __set__(self, instance, value):
        if value < 0:
            #raise ValueError('Cannot be negative.')
            print ('ValueError (''"Cannot be negative."'')')
        instance.__dict__[self.name] = value  # (6)

class Order:
    price = NonNegative('price')  # (3)
    quantity = NonNegative('quantity')
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity
apple_order = Order('apple', 1, 10)
print (apple_order.total())
apple_order1 = Order('apple', 1, 11)
# 10
apple_order.price = -10
# ValueError: Cannot be negative
apple_order.quantity = -10
# ValueError: Cannot be negative
print (apple_order1.total()) #Возвращает свое значение, т.к. у __dict__ есть идентификатор.