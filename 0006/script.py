# Problem 6  - Sum square difference
def sumSquare(num):
  sum = 0
  for x in range(1,num+1):
    sum += x
  return sum * sum

def sumPartialSquare(num):
  sum = 0
  for x in range(1,num+1):
    sum += x * x
  return sum

MAX = 100
print sumSquare(MAX) - sumPartialSquare(MAX)