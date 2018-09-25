# Problem 4  - Largest palindrome product
def isPalindron(num):
  s = str(num)
  return s == s[::-1]

data = set()
for x in range(100, 999):
  for y in range(100, 999):
    product = x * y
    if (isPalindron(product)):
      data.add(product)

print max(data)