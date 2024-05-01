class NegValException(Exception):
   pass

try:
   val = -1
   if val < 0:
       raise NegValException("Neg val: " + str(val))
   print(val + 10)
except NegValException as e:
  print(e)