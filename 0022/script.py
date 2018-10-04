# Problem 22 - Names scores
import math
import time as T

class Counter:
  name = None
  list = list()

  # ctor
  def __init__(self, name):
    self.name = name

  # read from file
  def readfile(self):
    with open(self.name) as f:
      self.list = f.read().replace('"', '').split(',')
      self.list.sort()

  # list of all dividers
  def score(self, name):
    chars = list(map(ord,list(name))) # list(name)
    chars = [x - 64 for x in chars]
    return sum(chars)
    


# init & count
start=T.time()
counter = Counter("0022/names.txt")
counter.readfile()
s = 0
i = 0
for n in counter.list:
  i += 1
  #if (n == 'COLIN'):
  #print (n, counter.score(n), i)
  s += counter.score(n) * i
print s

#print counter.score('COLIN')
print("Executed in {0:.2f} sec").format(T.time()-start)