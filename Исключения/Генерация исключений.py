try:
   raise Exception("Some exception")
except Exception as e:
   print("Exception exception " + str(e))