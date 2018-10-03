# Problem 19 - Counting Sundays
import math
import time as T
from datetime import date
from dateutil.relativedelta import relativedelta

class SundayCounter:
  list = list()

  # ctor
  def __init__(self):
    None

  # count sunday
  def count(self, start, end):
    sum = 0
    temp = start
    while temp <= end:
      if temp.weekday() == 6:
        if (temp.day == 1):
          sum += 1
      temp += relativedelta(days=1)
    return sum

# init & count
start=T.time()
counter = SundayCounter()
# 1 Jan 1901 to 31 Dec 2000
print counter.count(date(1901, 1, 1), date(2000, 12, 31))

print("Executed in {0:.2f} sec").format(T.time()-start)