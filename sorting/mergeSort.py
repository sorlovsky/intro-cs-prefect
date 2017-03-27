def merge(left, right):
    """TODO: Docstring for merge.

    :right: TODO
    :returns: TODO

    """
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while len(left) != 0:
        result.append(left[0])
        left = left[1:]

    while len(right) != 0:
        result.append(right[0])
        right = right[1:]

    return result



def mergeSort(lst):
    """TODO: Docstring for mergeSort.
    :returns: TODO

    """
    if len(lst) == 1:
        return lst

    left = []
    right = []
    for i in range(len(lst)):
        if i < len(lst)//2:
            left.append(lst[i])
        else:
            right.append(lst[i])

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

print(mergeSort([1, 2, 7, 2, 4, 1, 3]))
