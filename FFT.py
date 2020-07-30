test=int(input())
for i in range(test):
    sent=int(input())
    count=0
    new=[]
    ready=[]
    for k in range(sent):
        ready.append(str(input()))
        if k>=2:
            if (ready[k-2][0]+ready[k-1][0]+ready[k][0])=='FFT':
                count=count+1
                new.append(ready[k-2]+' '+ready[k-1]+' '+ready[k])
    if count==0:
        print(count)
    else:
        print(count)
        for s in range(count):
                    print(new[s])
            

            
