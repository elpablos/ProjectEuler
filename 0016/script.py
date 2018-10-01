# Problem 16 - Power digit sum
import math
import time as T
start=T.time()

DIM = 1000
print 

sum = 0
for c in str(int(math.pow(2, DIM))):
  sum += int(c)

print sum
print("Executed in {0:.2f} sec").format(T.time()-start)