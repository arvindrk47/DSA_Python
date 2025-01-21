import time
import threading

def display(x):
    for i in range(5):
        time.sleep(i+x)
        print(threading.current_thread().getName())
        print("thread started")

for p in range(5):
    t = threading.Thread(target=display, args=(p,))
    t.setName("Thread #"+str(p))
    t.start()