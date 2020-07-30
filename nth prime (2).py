def primebetter2(n):
    if n%2==0:
        return False
    else:
        maximum=n**0.5+1
        for x in range(3,int(maximum),2):
            if n%x==0:
                return False
                break
        else:
            return True
def create():
    global value
    value=[]
    for i in range(3,500000):
        if primebetter2(i)==True:
            value.append(i)
   
num=int(input())
create()
print(value[num])
    


        
