num=int(input())
for i in range(num):
    string=list(input())
    ucount=string.count('U')
    pcount=string.count('P')
    ccount=string.count('C')
    if ucount==0 or pcount==0 or ccount<=1:
        print('0')
    else:
        if ucount*2>ccount and pcount*2>ccount:
            print(int(ccount/2))
        elif ucount>pcount and ccount>=2*pcount:
            print(pcount)
        elif pcount>ucount and ccount>=2*ucount:
            print(ucount)
        else:
            print('0')
