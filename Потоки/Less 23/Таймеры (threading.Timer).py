from threading import Timer
from time import sleep, time
#Timer(interval, function, args=None, kwargs=None)
timer = Timer(interval=3,function=lambda: print("Message from Timer!"))
timer.start()