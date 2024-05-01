def method_decor(fn):
   def wrapper(self):
       print("Run method: " + str(fn.__name__))
       fn(self)
   return wrapper

class Vector():
   def __init__(self, px = 0, py = 0):
       self.px = px
       self.py = py
   @method_decor
   def norm(self):
       print((self.px**2 + self.py**2)**0.5)

vc = Vector(px=10, py=5)
vc.norm()