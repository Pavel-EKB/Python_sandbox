from threading import Thread, Lock
from time import sleep
def func():
    for i in range(5):
        print(f"from child thread: {i}")
        sleep(0.5)
th = Thread(target=func, daemon=True)
th.start()
print("App stop")