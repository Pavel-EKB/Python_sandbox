def decor_with_return(fn):
   def wrapper(*args, **kwargs):
       print("Run method: " + str(fn.__name__))
       return fn(*args, **kwargs)
   return wrapper

@decor_with_return
def calc_sqrt(val):
   return val**0.5

tmp = calc_sqrt(16)
print(tmp)