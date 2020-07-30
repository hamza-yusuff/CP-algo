import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

m=int(input())
n=int(input())
array=[]
for i in range(m):
   hello=list(map(int,input().split()))
   array.append(hello)
if m==2 and n==2:
    res=array[0][0]
    find=list(divisorGenerator(res))
    for k in range(len(find)):
        if find[k]>m and find[k]>n:
            find.remove(find[k])
    value='11'
    value='01'
    
    
