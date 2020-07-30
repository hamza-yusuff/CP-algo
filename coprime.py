import math
num=int(input())
array=list(map(lambda x:math.gcd(num,x),[i for i in range(1,num+1)]))
print(array.count(1))
