def param_transfer(fn):
   def wrapper(arg):
       print("Run function: " + str(fn.__name__) + "(), with param: " + str(arg))
       fn(arg)
   return wrapper

@param_transfer
def print_sqrt(num):
   print(num**0.5)

print_sqrt(4)