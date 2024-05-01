print("start")
try:
   val = 0
   tmp = 10 / val
   print(tmp)
except ValueError:
   print("ValueError!")
except ZeroDivisionError:
   print("ZeroDivisionError!")
except:
   print("Error!")
print("stop")

print("start")
try:
   val = 'erwr'
   tmp = 10 / val
   print(tmp)
except ValueError as ve:
   print("ValueError! {0}".format(ve))
except ZeroDivisionError as zde:
   print("ZeroDivisionError! {0}".format(zde))
except Exception as ex:
   print("Error! {0}".format(ex))
print("stop")