#Finding Indexes from a List of Numbers Whose Total Sum is 9

def two_sum(nums,target):
    seen = {}

    for i,num in enumerate (nums):
        remain = target - num
        if remain in seen:
             return [seen[remain],i ]
        seen[num] = i
    return None

nums = [2,7,12,5]
target = 12

result = two_sum(nums,target)
print(f"For target {target} indexes are {result}")
