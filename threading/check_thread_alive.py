import threading
import time


def display(x):
    time.sleep(x)
    return

t1 = threading.Thread(target=display, args=(5,), name="Thread 1")
t1.start()
t2 = threading.Thread(target=display, args=(4,), name="Thread 2")
t2.start()


for x in range(5):
    time.sleep(x+0.5)
    print('[', time.ctime(), t1.name, t1.is_alive(),']')
    print('[', time.ctime(), t2.name, t2.is_alive(),']')