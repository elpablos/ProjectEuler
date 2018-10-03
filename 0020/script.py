# Problem 20 - Factorial digit sum
import math
import time as T

class Counter:
  list = list()

  # ctor
  def __init__(self):
    None

  # factorial
  def factorial(self, num):
    if (num < 2):
      return 1
    else:
      return self.factorial(num - 1) * num

  def numberSum(self, num):
    nums = list(map(int, list(str(num))))
    return sum(nums)

# init & count
start=T.time()
counter = Counter()
# factorial
f = counter.factorial(100)
print (f, counter.numberSum(f))

print("Executed in {0:.2f} sec").format(T.time()-start)