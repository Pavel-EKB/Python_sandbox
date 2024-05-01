class Rectangle:
    def __new__(cls, *args, **kwargs):
        print("Hello from __new__")
        return super().__new__(cls)
    def __init__(self, width, height):
        print("Hello from __init__")
        self.width = width
        self.height = height

rect = Rectangle(10, 20)
print (rect.width)
print (rect.height)