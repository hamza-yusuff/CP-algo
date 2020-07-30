test=int(input())
for i in range(test):
    n,m=map(int,input().split())
    hp=[]
    cost=[]
    for c in range(n):
        x,y=map(int,input().split())
        cost.append(x)
        hp.append(y)
    new=sorted(hp)
    happy=0
    add=0
    for k in range(n-1,-1,-1):
        lambo=cost[hp.index(new[k])]
        cost[hp.index(new[k])]=0
        hp[hp.index(new[k])]=0
        add=add+lambo
        if add>m:
            add=add-lambo
        else:
            happy=happy+new[k]
    print(happy)  
