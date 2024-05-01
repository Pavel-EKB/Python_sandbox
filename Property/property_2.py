import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area

    @property
    def circle_area(self):
        return self.radius ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print (p)

print (p.area())

print (p.circle_area)