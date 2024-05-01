from functools import update_wrapper

def x10(a):
   return a * 10
def some_mul(a: int) -> int:
   """a * some value"""
   return a * 1

wrapped_mul = update_wrapper(x10, some_mul)

print (wrapped_mul(3.55))

print (wrapped_mul.__name__)

print (wrapped_mul.__annotations__)

print (wrapped_mul.__doc__)
