def sumList(L):
    sum = 0
    for i in range(len(L)):
        sum = sum + L[i]
    return sum

def sumRecursive(L):
    print(L)
    if len(L) == 0:
        return 0
    return L[0] + sumRecursive(L[1:])

monkey = [1,2,4,5]
# print(sumList(monkey))
print(sumRecursive(monkey))
