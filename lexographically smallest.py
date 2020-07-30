l,k=map(int,input().split())
string=input()
counter=[]
done=[]
for i in range(l):
        
        if string.count(string[i])==k and string[i] not in done:
                counter.append(string[i])
        done.append(string[i])
if len(counter)!=0:
        f=sorted(counter)
        s=list(string)
        delete=f[len(f)-1]
        new=[]
        s.remove(delete)
        for j in range(k):
            sani=''.join(s)
            if sani<string:
                string=sani
                
        
        print(string)
        
else:
        print(string)
                        

