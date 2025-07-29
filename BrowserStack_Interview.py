#by Amaan Hakim (1167)   on 28/07/2025

#1.asked to make HLD of Autopause system (from resume)
# Project ka HLD banane bola, so draw.io pr banaya, 

# Explain kiya project on that, 

# Services wagera me deep me gaya tha, 

# API me depth me gaya, fastapi async... Etc

# Ispr hi 2 3 conditions diye if yeh hua toh tu kya krega. 

# Then, 
# In general prob, if kal meta rate limit krde, so usko overcome kaise kroge, like jo bhi ApI call we do on meta ads manager woh sab, 

# Fir DNS kaise work krta hai if ye toh kya krega etc etc.. 

# the integer data type does not support integers beyond 2 digits. 
# So, the int data type can store values up to say 99 or minus 99, but it cannot store 100. 
# Got it? I will give you two 4-digit integers asa buffer stream.get result of addition.
# # int no beyond 2 digit 10 - 99

# 2 4 digit int as buffer stream, result of addition

# 99 99 + 
# 88 88

#18887

# 99+88 = 187+0 = 87 -> 1 

# 99+88 = 187 + 1 = 188 -> 88 

# 1 88 87

def add_num(a,b):
    carry = 0
    result = ""
    
    i = len(a)
    while i >0:
        x = int(a[i-2:i]) if i-2 >=0 else int(a[0:i])
        y = int(b[i-2:i]) if i-2 >=0 else int(b[0:i])
        
        sum = x + y + carry 
        carry = sum //100
        result = str(sum % 100).zfill(2) + result
        i-=2
    if carry:
        result = str(carry) + result
    return result.lstrip("0")
    
print(add_num("9999","8888"))

        


