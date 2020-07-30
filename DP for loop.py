def fibonacci(n):
    memo={}
    for i in range(1,n+1):
        if i==1 or i==2:
            f=1
        else:
            f=memo[i-1]+memo[i-2]
        memo[i]=f
    return memo[n]
print(fibonacci(12)%1000000007)
