import time
import _thread

def a(msg):
    ct = 0
    while ct< 5:
        print(msg)
        time.sleep(3)
        ct+=1
    
def b(msg):
    ct=0
    while ct<5:
        print(msg)
        time.sleep(5)
        ct+=1

try:
    _thread.start_new_thread(a, ('Thread a',))
    _thread.start_new_thread(b, ('thread b',))

except:
    print("Error is occuring ")

while 1:
    pass