def primebetter2(n):
    if n==1:return False
    if n==2:return True
    if n%2==0 and n!=2:
        return False
    else:
        maximum=n**0.5+1
        for x in range(3,int(maximum),2):
            if n%x==0:
                return False
                break
        else:
            return True
print(primebetter2(1))
test=int(input())
for i in range(test):
    num=int(input())
    root=(num)**0.5
    if primebetter2(int(root))==True:
        print('YES')
    else:
        print('NO')

