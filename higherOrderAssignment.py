import functools
import operator

def thread(f, l1, l2):
    return map(lambda i: f(l1[i], l2[i]), range(len(l1)))
    # result = []
    # for i in range(len(l1)):
    #     result += [f(l1[i], l2[i])]

def add(a, b):
    return a + b

def dot(l1, l2):
    return functools.reduce(operator.add, thread(operator.mul, l1, l2))

l = [5]


def mystery(n):
    l = list(range(2, n))
    while len(l) != 0:
        print(l[0])
        l = list(filter(lambda x: x%l[0]==1, l))
    return None

def isDivisibleBy(n):
    return lambda x: x%n==0

def main():
    l1 = [1, 2, 4, 5]
    l2 = [3, 1, 1, 4]
    # print(dot(l1, l2))
    # mystery(10)
    # for i in range(len(l1)):
    #     print(range(0,4))
    # mystery(100)
    # print(list(thread(operator.add, l1, l2)))
    isDivisibleBy7 = isDivisibleBy(8)
    print(isDivisibleBy7(14))
main()
