# Problem 12 - Highly divisible triangular number
import math
import time as T
start=T.time()

def isPrime(n):
  if n % 2 == 0 and n > 2: 
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

primes = [2,3,5,7,11,13,17,19]

def getPrimeDividers(num):
  data = list()
  for p in primes:
    while num % p == 0 and num > 0:
      data.append(p)
      num /= p

  if num > 1:
    if(isPrime(num)):
      data.append(num)
    else:
      i = max(primes)
      while num > 0 and i <= num:
        if isPrime(i) and num % i == 0:
          data.append(i)
          num /= i
        else:
          i += 2
  return data

def per(n):
  data = list()
  for i in range(1<<n):
    s=bin(i)[2:]
    s='0'*(n-len(s))+s
    o = map(int,list(s))
    data.append(o) 
  return data

def getDividers(inp):
  data = set()
  for c in per(len(inp)):
    sum = 1
    for i in range(len(inp)):
      if c[i] > 0:
        sum *= c[i] * inp[i]
    data.add(sum)
  return data

#result
data = set()
TOP = 500
i = 1
sum = 0
while len(data) < TOP:
  sum += i
  data = getPrimeDividers(sum)
  data = getDividers(data)
  # print (i, len(data))
  i += 1

# print data
print (max(data), len(data), i)
print("Executed in {0:.2f} sec").format(T.time()-start)