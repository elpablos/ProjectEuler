# Problem 2 - Even Fibonacci numbers

def Fibonacci(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num - 1) + Fibonacci(num - 2)

data = set()
for x in range(2,1000,1):
    fib = Fibonacci(x)
    if fib < 4000000:
        if fib % 2 == 0:
            data.add(fib)
    else:
        break
    print('{0}: {1}').format(x, fib)
print ('suma: {0}').format(sum(int(i) for i in data))