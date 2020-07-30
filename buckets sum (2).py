while 1:
    x,y=map(int,input().split())
    if x==y==0:
        break
    else:
        buckets=y-x+1
        n=y-x+1
        total=(n/2)*(2*x+(n-1))
        print(buckets, int(total))
