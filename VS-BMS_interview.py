#https://leetcode.com/problems/trapping-rain-water/description/
#Trapping Rain Water Question from Leetcode - 
#Asked In BookMyShow DSA Round for SDE 1 - 

def watertrapped(heights):
    n = len(heights)
    total_water = 0

    for i in range(n):
        max_left =max(heights[:i+1])
        max_right = max(heights[i:])

        total_water += min(max_left,max_right)-heights[i]

    return total_water

heights = [2, 1, 5, 3, 1, 0, 4]
print(watertrapped(heights)) 