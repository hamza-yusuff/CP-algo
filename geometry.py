a,b=input().split()
a=int(a)
b=int(b)
if a>=b:possible=(a+b)-(a-b)-1
if b>a:possible=(a+b)-(b-a)-1
print(possible)
