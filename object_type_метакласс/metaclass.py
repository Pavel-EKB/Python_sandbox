def upper_attr(future_class_name, future_class_parents, future_class_attr):
    # берем любой атрибут, не начинающийся с '__'
    print (future_class_attr.items())
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # переводим их в верхний регистр
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)

    # создаем класс с помощью 'type'
    return type(future_class_name, future_class_parents, uppercase_attr)

class Foo(metaclass = upper_attr):
    bar = 'bip'
    bor = 'bop'

print (hasattr(Foo, 'bar'))
# Out: False
print (hasattr(Foo, 'BAR'))
# Out: True

f = Foo()
print (f.BAR)
print (f.BOR)
# Out: 'bip'