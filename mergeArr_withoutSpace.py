def mergeSortedArrays(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j = n-1, 0

    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()
    return arr1 + arr2


arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
print(mergeSortedArrays(arr1,arr2))
