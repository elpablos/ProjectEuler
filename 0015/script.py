# Problem 15 - Longest Collatz sequence
import math
import time as T
start=T.time()

def getRoutes(n):
  data = list()
  i = 0
  half = n / 2
  max = (1 << n)
  while i < max:
    s=bin(i)[2:]
    s='0'*(n-len(s))+s
    o = map(int,list(s))
    if (sum(o) == half):
      data.append(o) 
    i += 1
  return data

def getLightRoutes(n):
  ss = 0
  i = n
  half = n / 2
  max = (1 << n)
  while i < (max/2):
    s=bin(i)[2:]
    s='0'*(n-len(s))+s
    o = map(int,list(s))
    if (sum(o) == half):
      ss += 1
    i += 1
  return ss * 2

def makeBitWord(i, n):
  s=bin(i)[2:]
  s='0'*(n-len(s))+s
  return s

DIM = 20
# print (DIM, getLightRoutes(DIM + DIM))

# https://math.stackexchange.com/questions/400041/number-of-equivalent-rectangular-paths-between-two-points
print math.factorial(DIM + DIM) / (math.factorial(DIM)*math.factorial(DIM))

print("Executed in {0:.2f} sec").format(T.time()-start)