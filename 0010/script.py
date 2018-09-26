# Problem 10  - Summation of primes
import math

# Even if you are going to brute-force for prime like this 
# you only need to iterate up to the square root of n. Also, 
# you can skip testing the even numbers after two.
def isPrime(n):
  if n % 2 == 0 and n > 2: 
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0:
      return False
  return True

MAX = 2000000
sum = 0
for x in range(2, MAX):
  if (isPrime(x)):
    sum += x

print sum