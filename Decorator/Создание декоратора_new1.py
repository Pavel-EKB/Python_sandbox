import time

def timer(func):
   def wrapper(*args, **kwargs):
       print(f"{func.__name__!r} begins")
       start_time = time.time()
       print (list(args))
       val = (f"Возврат из timer - {func(*args, **kwargs)}")
       print(f"{func.__name__!r} ends in {time.time()-start_time}  secs")
       return val
   return wrapper

@timer
def somefunc(a, b):
    output = a+b
    print (f"{output} - from somefunc")
    return output

a = somefunc(4,5)
print (a)