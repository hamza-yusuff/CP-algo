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
def case(num):
    array=[]
    length=len(num)
    for i in range(int(length/2)):
        res=num[i:i+4]
        for c in range(10):
          res=res[i:c]
          if int(res)<10000 and int(res)>1 :
             primebetter2(int(res))
             if primebetter2==True:
                 array.append(int(res))
    return array
test=int(input())
for k in range(test):
    x,y=input().split()
    primes=case(x)
    print('Case {}:'.format(k+1),max(primes))

    

