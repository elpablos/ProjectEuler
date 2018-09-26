# Problem 14 - Longest Collatz sequence
import math
import time as T
start=T.time()

known = dict()

def collatz(known, num):
  data = list()
  temp = num
  while temp > 1:
    if temp in known:
      for i in known[temp]:
        data.append(i)
      break
    data.append(temp)
    if temp % 2 == 0:
      temp /= 2
    else:
      temp = temp * 3 + 1
  else:
    data.append(temp)
  return data

# print data
NUM = 1000000
l = -1
d = list()
for i in range (1,NUM):
  data = collatz(known, i)
  known[i] = data
  if (l < len(data)):
    l = len(data)
    d = data
print (l, d[0])

print("Executed in {0:.2f} sec").format(T.time()-start)