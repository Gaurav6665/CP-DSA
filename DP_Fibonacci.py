
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n<=0:
        result= 0
    if n<=2:
        result= 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return memo[n]

#input 
#n = int(input("Enter n = "))
n=50
print(fib(n))


#####################################################################

#Recurtion + Memoization

def fib(n):
    memo={}
    for i in range(1,n+1):
        if i<=2:
            result=1
        else:
            result = memo[i-1] + memo[i-2]
        memo[i] = result
    return memo[n]

n=50
print(fib(n))
