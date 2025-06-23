#binary search element problem

def binary_search(arr,target):
    l,r = 0,len(arr)-1

    while l<=r:
        m = (l+r)//2
        if arr[m] == target:
            return m 
        elif arr[m] < target:
            l = m+1
        else:
            r = m-1
    return -1

arr = [1,2,3,4,5,6,7,8,9]
target = 8
result = binary_search(arr,target)
print(f"{target} is at index {result} of {arr}")