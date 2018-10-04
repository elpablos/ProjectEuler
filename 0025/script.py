# Problem 25 - 1000-digit Fibonacci number
import math
import time as T

class Counter:
  # ctor
  def __init__(self):
    None

  def Fibonacci(self, num):
      if num <= 0:
          return 0
      elif num == 1:
          return 1
      else:
          return self.Fibonacci(num - 1) + self.Fibonacci(num - 2)

# init & count
start=T.time()
counter = Counter()

LVL = 1000

last = 1
prelast = 0
inc = 1
temp = 1

while True:
  inc += 1
  
  temp = last + prelast
  prelast = last
  last = temp

  if len(str(temp)) == LVL:
    print inc # (inc, temp)
    break
  

print("Executed in {0:.2f} sec").format(T.time()-start)