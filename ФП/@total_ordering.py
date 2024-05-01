from functools import total_ordering

@total_ordering
class Rational:
   def __init__(self, a, b):
       self.num = a
       self.den = b
   def __lt__(self, other):
       return (self.num / self.den) < (other.num / other.den)
   def __eq__(self, other):
       return (self.num == other.num) and (self.den == other.den)

a = Rational(1, 2)
b = Rational(3, 4)
print (a < b)

print (a <= b)

print (a == b)

print (a >= b)

print (a > b)