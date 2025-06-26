# Write a function to count the number of unique digits in a number - 
# eg 111 -> 1 
# 121 -> 2 
# 123 -> 3
# num = -121.553
# print(len(set(str(abs(num)))))

# def unique_cnt(num):
    
#     num_str =str(abs(num))
#     unique = set()
    
#     for i in num_str:
#         if '0' <= i <= '9':
#             unique.add(i)
#     print(len(unique))
    
# unique_cnt(num)

# Given a List of n integers and a number k, find the pairs of numbers in the list 
# such that the difference between the pair is k.

# nums = [1,2,3,4,5,6,7]
# k =2 

# o/p = (1,3)

# def pairs(nums,k):
#     n=len(nums)
#     result = []
    
#     for i in range(n):
#         for j in range(i+1,n):
#             dif = num[j] - num[i]
#             if dif == k:
#                 result.append((num[i],num[j]))

# def pairs(nums,k):
#     seen =set(nums)
#     res = set()
    
#     for i in nums:
#         if i + k in seen:
#             res.add((i,i+k))
#         if i - k in seen:
#             res.add((i-k,i))
#     print(res)
# you are given a string s and an integer t, representing the number of transformations 
# to perform. In one transformation, every character in s is replaced according to the 
# following rules:
    
# If the character is 'z', replace it with the string "ab".

# Otherwise, replace it with the next character in the alphabet. 
# For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.

# Return the length of the resulting string after exactly t transformations.

# Input: s = "abcyy", t = 2
# Output: 7
# Explanation:
# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.
# Since the answer may be very large, return it modulo 109 + 7.            

s = "abcyy"
t = 2
# Input: s = "abcyy", t = 2
# Output: 7
# cdeabab
# def transform(s,t):
#     for i in range(t):
#         new_str = ""
#         for ch in s:
#             if ch == 'z':
#                 new_str += 'ab'
#             else:
#                 nxt_chr = chr(ord(ch)+1)
#                 new_str += nxt_chr
#             s = new_str
#         print (len(s)) % MOD
# transform(s,t)




    
                

                
        
    


