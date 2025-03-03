import time
import multiprocessing
start = time.perf_counter()


def do_something():
    print('Sleeping 1 second.....')
    time.sleep(3)
    print('Done Sleeping.....')

p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)
p1.start()
p2.start()


finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')
