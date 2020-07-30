import math
def combination(num,k):
    res=(math.factorial(num)/(math.factorial(num-k)*math.factorial(k)))
    return res
test=int(input())
for i in range(test):
    number=int(input())
    add=0
    for f in range(number+1):
        if f%2==0:
                add=add+combination(number,f)
        elif f%2!=0:
                add=add-combination(number,f)
    print(int(add))
    
