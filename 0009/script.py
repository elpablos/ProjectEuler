# Problem 9  - Special Pythagorean triplet
def findTriplet(num):
  a = b = c = 0
  while True:
    b = 0
    while b < c:
      a = 0
      while a < b:
        if ((a * a) + (b * b)) == (c * c):
          # print('a: {0}, b: {1}, c: {2}, sum: {3}').format(a,b,c,(a + b + c))
          if ((a + b + c) == num):
            print 'FIND!'
            return (a,b,c)
        a += 1
      b += 1
    c += 1

TARGET = 1000
(a,b,c) = findTriplet(TARGET)

print('a: {0}, b: {1}, c: {2}, sum: {3}, product: {4}').format(a,b,c,(a + b + c), a*b*c)

