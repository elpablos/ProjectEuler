# Problem 26 - Reciprocal cycles
import math
import time as T

class Counter:
  # ctor
  def __init__(self):
    None

  def fraction(self, num, limit):
    res = list()
    temp = 1
    inc = 0
    while temp % num != 0 and inc < limit:
        res.append(temp / num)
        temp = (temp % num) * 10
        inc += 1
    else:
        res.append(temp / num)
    return res

# init & count
start=T.time()
counter = Counter()

print counter.fraction(7, 25)

for i in range(1, 21):
    print (i, counter.fraction(i, 20))

print("Executed in {0:.2f} sec").format(T.time()-start)