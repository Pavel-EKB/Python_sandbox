class UserLevel():
   us_dict = {"Admin":4, "Operator":3, "Dispatcher":2, "Guest":1}
   def __init__(self, user_level):
       if user_level in self.us_dict:
           self.u_level = user_level
       else:
           print("Wrong user type!")
           self.u_level = "Guest"
   def diff(self, level1, level2):
       return self.us_dict[level1] - self.us_dict[level2]
   def __lt__(self, user):
       return True if self.diff(self.u_level, user.u_level) < 0 else False

   def __le__(self, user):
       return True if self.diff(self.u_level, user.u_level) <= 0 else False
   def __eq__(self, user):
        return True if self.diff(self.u_level, user.u_level) == 0 else False
   def __ge__(self, user):
        print ('self = '+self.u_level+', user = '+user.u_level)
        return True if self.diff(self.u_level, user.u_level) >= 0 else False
   def __gt__(self, user):
       return True if self.diff(self.u_level, user.u_level) > 0 else False
   def __repr__(self):
       return "UserLevel({})".format(self.u_level)
   def __str__(self):
       return self.u_level
if __name__ == "__main__":
   need_level = UserLevel("Operator")
   print("need level: {}".format(need_level))
   user_level = UserLevel("Dispatcher")
   print("user: {}".format(user_level))
   if user_level >= need_level:
       print("Access enabled!")
   else:
       print("Access denied!")

print ('\n---------------------------------------')

class Vector():
   def __init__(self, x, y):
       self.x = x
       self.y = y
   def __add__(self, v):
       return Vector(self.x + v.x, self.y + v.y)
   def __sub__(self, v):
       return Vector(self.x - v.x, self.y - v.y)
   def __repr__(self):
       return "Vector({}, {})".format(self.x, self.y)
   def __str__(self):
       return "({}, {})".format(self.x, self.y)
   def __abs__(self):
       return (self.x**2 + self.y**2)**0.5

if __name__ == "__main__":
   v1 = Vector(3, 4)
   print("vector v1 = {}".format(v1))
   v2 = Vector(5, 7)
   print("vector v2 = {}".format(v2))
   print("v1 + v2 = {}".format(v1 + v2))
   print("v2 - v1 = {}".format(v2 - v1))
   print("|v1| = {}".format(abs(v1)))

print ('\n---------------------------------------')

class Test ():
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
       return "({}, {})".format(self._a, self._b)

t = Test (1, 2)
print (t)
