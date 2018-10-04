# Problem 21 - Amicable numbers
import math
import time as T

class Counter:
  list = list()

  # ctor
  def __init__(self):
    None

  # list of all dividers
  def divisors(self, num):
    nums = list()
    for i in range(1, num):
      if (num % i == 0):
        nums.append(i)
    return nums

  # If d(a) = b and d(b) = a, where a != b 
  def amicable(self, a):
    b = sum(counter.divisors(a))
    return (a != b and sum(counter.divisors(b)) == a, a, b)


# init & count
start=T.time()
counter = Counter()
# sum of amicable
amb = set()
for x in (range(1, 10001)):
  (iz, a, b) = counter.amicable(x)
  if (iz):
    amb.add(a)
    amb.add(b)
print sum(amb)

print("Executed in {0:.2f} sec").format(T.time()-start)