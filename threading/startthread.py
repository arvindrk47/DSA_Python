import time
import threading

def display(x,t1, name):
    for i in range(x):
        time.sleep(t1)
        print(f"{name} started")

t = threading.Thread(target=display, args=(5,2,"Thread 1",))
t.start()
t3 = threading.Thread(target=display, args=(6,2,"Thread 2",))
t3.start()
