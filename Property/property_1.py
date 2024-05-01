class Mine(object):

    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        self._x = 'No more'

    x = property(get_x, set_x, del_x, 'Это свойство x.')

type(Mine.x)  # property
mine = Mine()
print(mine.x)  # None
mine.x = 3
print(mine.x)  # 3
del mine.x
print(mine.x)  # No more