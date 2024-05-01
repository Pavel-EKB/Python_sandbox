class Slotter:
    __slots__ = ["a", "b"]

s = Slotter()
#s.__dict__      # AttributeError
#s.c = 1         # AttributeError
s.a = 1
print(s.a)             # 1
s.b = 1
print(s.b)             # 1
print(dir(s))          # [ ... 'a', 'b' ... ]