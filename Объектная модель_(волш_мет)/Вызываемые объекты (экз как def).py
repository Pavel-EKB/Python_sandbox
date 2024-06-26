class Entity:
    '''Класс, описывающий объект на плоскости. "Вызываемый", чтобы обновить позицию объекта.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Изменить положение объекта.'''
        self.x, self.y = x, y

if __name__ == "__main__":
    test = Entity(10, 1, 1)
    print ("x=%d, y=%d" %(test.x, test.y))
    test (8, 9)
    print ("x=%d, y=%d" %(test.x, test.y))

    print('OK')
