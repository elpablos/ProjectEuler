# Problem 23 - Non-abundant sums
import math
import time as T

class Counter:
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
    
# init & count
start=T.time()
counter = Counter()

TARGET = 28123 + 1 # 28123
abudant = {12, 18}
sumabudant = set()
for x in range(1, TARGET):
  s = sum(counter.divisors(x))
  # is abudant number
  if (x < s):
    abudant.add(x)
    # print (x,s)
  # detect no abudant
  #if (x not in abudant):
  for y in abudant:
    temp = (x - y)
    if temp in abudant:
      sumabudant.add(x)
      break

nonabundant = set(range(1, TARGET)) - sumabudant # abudant
print (len(nonabundant), sum(nonabundant))

print("Executed in {0:.2f} sec").format(T.time()-start)