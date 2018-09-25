# Problem 7  - 10001st prime
def isPrime(num):
  a = 2
  # vsechna prvocisla jsou licha vyjma 2
  if num == 2:
    return True
  elif num % 2 == 0:
    return False

  while num > a:
    if num % a == 0:
      return False
    a += 1
  return True

MAX = 10001
counter = 0
i = 1
while counter < MAX:
  i += 1
  if isPrime(i):
    # print i
    counter += 1

print i