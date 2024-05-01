class Mine(object):

    def __init__(self):
        self._x = 'some value'

    @property
    def prop(self):
         return self._x

mine = Mine()
print(mine.prop)  # some value
mine.prop = 'other value'  # AttributeError
del mine.prop  # AttributeError