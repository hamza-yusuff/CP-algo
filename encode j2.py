lines=int(input())
num=[]
for i in range(lines):
    x,y=input().split()
    num.append(int(x)*y)
for k in range(lines):
    print(num[k])
    
