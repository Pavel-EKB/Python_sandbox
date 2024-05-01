class UpperAttrMetaclass(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)

        return type.__new__(cls, name, bases, uppercase_attr)

class Foo(metaclass = UpperAttrMetaclass):
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