def primeNumbers(n):
    l = list(range(2, n))
    primes = []
    while len(l) != 0:
        primes.append(l[0])
        l = list(filter(lambda x: x%l[0]!=0, l))
    return primes

print(primeNumbers(100))

