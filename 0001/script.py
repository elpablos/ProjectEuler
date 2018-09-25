# Problem 1 - Multiples of 3 and 5
limit = 1000
primes = [3, 5]
data = set()
for prime in primes:
    for x in range(prime, limit, prime):
        data.add(x)
print sum(int(i) for i in data)