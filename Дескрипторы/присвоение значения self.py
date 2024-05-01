class MyDescriptor(object):
    """Это класс дескриптора."""

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        # Зачастую здесь возвращают значение, хранящееся в instance -
        # см. my_owner ниже.
        return self.value

    def __set__(self, instance, value):
        # Зачастую значение сохраняется в instance (см. my_owner ниже),
        # для демонстрации сохраним его в объекте
        # дескриптора.
        self.value = value


class MyOwner(object):
    """Это класс владелец дескрипторов."""

    field1 = MyDescriptor('one')
    field2 = MyDescriptor('two')


my_owner = MyOwner()
print (my_owner.field1)  # one
my_owner.field1 = 1
print (my_owner.field1)  # 1

# Мы храним присвоенное значение в объекте дескриптора,
# являющимся общим для всех наследников класса, а потому:
my_owner2 = MyOwner()
print (my_owner2.field1)  # 1

my_owner.__dict__['field1'] = 'some'
print (my_owner.field1)  # 1
print (my_owner.__dict__['field1'])