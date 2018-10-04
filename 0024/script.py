# Problem 24 - Lexicographic permutations
import math
import time as T

class Counter:
  # ctor
  def __init__(self):
    None

  # permutation
  def heaps(self, n, a):
    iter = list()
    c = [0]*n
    i = 0
    iter.append(''.join(a))
    while i < n:
      if  c[i] < i:
        if (i%2)==0:
          a[0],a[i] = a[i],a[0]
        else:
          a[c[i]],a[i] = a[i],a[c[i]]
        # print(a)
        iter.append(''.join(a))
        c[i] += 1
        i = 0
      else:
        c[i] = 0
        i += 1
    return iter
    
# init & count
start=T.time()
counter = Counter()

MAX = 9
printed = 1000000

input = map(str,list(range(MAX+1)))
x = counter.heaps(len(input),input)

x.sort()
print x[printed-1]

print("Executed in {0:.2f} sec").format(T.time()-start)