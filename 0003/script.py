# Problem 3 - Largest prime factor
num = 600851475143
temp = num
data = set()

while temp > 1:
  a = 2
  while temp >= a :
    if temp % a == 0:
      print('Prime: {0}').format(a)
      data.add(a)
      temp = temp / a
      break
    a += 1

print max(data)