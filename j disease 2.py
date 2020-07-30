import math
p=int(input())
before=int(input())
grow=int(input())
if grow!=1:
    res=(p*(grow-1)+1)/before
    num=math.log(res,grow)
    print(int(num))
elif grow==1:
    res=[before,before*grow]
    i=2
    while sum(res)<=p:
       res.append(res[i-1]*grow)
       i=i+1
    print(i-1)
