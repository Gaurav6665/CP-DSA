def next_greater_element(arr):
    result = []
    for i in range(len(arr)):
        next_greater = -1

        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                next_greater = arr[j]
                break
        result.append(next_greater)
    return result

arr= [4, 5, 2, 10, 8]
result = next_greater_element(arr)
print(f"Next greater element for {arr} is {result}")