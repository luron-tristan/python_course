# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading

# multiprocessing = better for cpu bound tasks (heavy cpu usage)
# multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time

def counter(num):
  count = 0
  while count < num:
    count += 1

def main():

  print(cpu_count())

  num = 1000000000
  divider = num / 8

  a = Process(target=counter, args=(divider,))
  a.start()
  
  b = Process(target=counter, args=(divider,))
  b.start()

  c = Process(target=counter, args=(divider,))
  c.start()
  
  d = Process(target=counter, args=(divider,))
  d.start()
  
  e = Process(target=counter, args=(divider,))
  e.start()
  
  f = Process(target=counter, args=(divider,))
  f.start()

  g = Process(target=counter, args=(divider,))
  g.start()
  
  h = Process(target=counter, args=(divider,))
  h.start()

  a.join()
  b.join()
  c.join()
  d.join()
  e.join()
  f.join()
  g.join()
  h.join()

  print("finished in:", time.perf_counter(), "seconds")

if __name__ == "__main__":
  main()