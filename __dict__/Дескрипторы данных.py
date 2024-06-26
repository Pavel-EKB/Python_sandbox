class DataDesc:

    def __get__(self, obj, cls):
        print("Trying to access from {0} class {1}".format(obj, cls))

    def __set__(self, obj, val):
        print("Trying to set {0} for {1}".format(val, obj))

    def __delete__(self, obj):
        print("Trying to delete from {0}".format(obj))

class DataHolder:
        data = DataDesc()
d = DataHolder()

DataHolder.data # Trying to access from None class <class '__main__.DataHolder'>
d.data          # Trying to access from <__main__.DataHolder object at ...> class <class '__main__.DataHolder'>
d.data = 1      # Trying to set 1 for <__main__.DataHolder object at ...>
del(d.data)     # Trying to delete from <__main__.DataHolder object at ...>

#Проверим утверждение о том, что у дата дескрипторов преимущество перед записями в __dict__ экземпляра
d.__dict__["data"] = "override!"
d.__dict__  # {'data': 'override!'}
d.data      # Trying to access from <__main__.DataHolder object at ...> class <class '__main__.DataHolder'>

#Если изменить значение атрибута с дескриптором через класс
DataHolder.__dict__ # {...'data': <__main__.DataDesc object at ...>...}
DataHolder.data = "kick descriptor out"
DataHolder.__dict__ # {...'data': 'kick descriptor out'...}
DataHolder.data     # "kick descriptor out"