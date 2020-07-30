def prime(n):
    prime=[True for i in range(n+1)]
    p=2
    while (p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p=p+1
    return prime
f=prime(40)
for k in range(2,41):
    if f[k]==True:
        print(k)
    
