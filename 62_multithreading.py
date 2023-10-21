# thread = a flow of execution. Like a separate order of instructions.
# However, each thread takes a turn running to achieve concurrency
# GIL = global interpreter lock,
# allow only one thread to hold the control of the Python interpreter at any one time

# cpu bound: program/task that spends most of it's time waiting for internal events (CPU intensive)
# use multiprocessing

# io bound: program/task that spends most of it's time waiting for external events (user input, web scraping)
# use multithreading

import threading
import time

def brush_teeth():
  time.sleep(3)
  print("You brushed your teeth")

def drink_coffee(value):
  time.sleep(4)
  print("You drank your coffee with", value)

def shower():
  time.sleep(5)
  print("You get out of the shower")

# drink_coffee("stevia")
# brush_teeth()
# shower()

x = threading.Thread(target=drink_coffee, args=("sugar",))
x.start()

y = threading.Thread(target=brush_teeth)
y.start()

z = threading.Thread(target=shower)
z.start()

x.join() # main thread waits for thread to finish
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
