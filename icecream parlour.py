test=int(input())
for i in range(test):
    taka=int(input())
    num=int(input())
    f=list(map(int,input().split()))
    s=[]
    for i in range(taka):
        res=taka-i
        if i in f and res in f:
            if f.index(res)==f.index(i):
                s.append(f.index(res)+1)
                f[f.index(res)]=''
                s.append(f.index(i)+1)
                break
            else:
                s.append(f.index(res)+1)
                s.append(f.index(i)+1)
                break
    s.sort()
    print(s[0],s[1])
