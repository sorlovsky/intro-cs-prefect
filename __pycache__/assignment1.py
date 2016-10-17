def isOdd(num):
    return num%2 == 1

def isPrime(num):
    divider=1
    while(divider < num):
        if num % divider == 0 and num != divider and divider != 1:
            return False
        divider = divider+1
    return True

def paul(n, k):
    if n % 2 == 0:
        return paul(n // 2, k)
    else:
        return paul(3 * n + k, k)

def test(k):
    for i in range(100):
        print(paul(i, k))

def main():
    paul(4, 3)


main()
