# Problem 5  - Smallest multiple
MAX = 20
def isDivinible(num):
  for x in range(1,MAX+1):
    if num % x != 0:
      return False
  return True

def isPrime(num):
  a = 2
  while num > a:
    if num % a == 0:
      return False
    a += 1
  return True

data = set()
# sum = 1
# for x in range(1,MAX+1):
#   sum *= x

# print sum

x = 1
while isDivinible(x) == False:
  x += 1

print x