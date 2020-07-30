

number=int(input())
read=[]
for i in range(number):
    read.append(int(input()))
if len(read)==len(set(read)):
    print(max(read)-min(read))
else:
    rep=list(set(read))
    freq=list(map(lambda x:read.count(x),rep))
    high=rep[freq.index(max(freq))]
    if len(freq)==len(set(freq)):
        freq.remove(max(freq))
        rep.remove(high)
        secondhigh=rep[(freq.index(max(freq)))]
        print(abs(high-secondhigh))
    else:
        highest=[high]
        hell=max(freq)
        rep.remove(rep[freq.index(max(freq))])
        freq.remove(max(freq))
        while hell in freq and len(freq)>0:
            highest.append(rep[freq.index(max(freq))])
            rep.remove(rep[freq.index(max(freq))])
            freq.remove(max(freq))
        if len(highest)==1:
            hell2=max(freq)
            lower=rep[freq.index(hell2)]
            secondhighest=[lower]
            rep.remove(rep[freq.index(hell2)])
            freq.remove(hell2)
            while hell2 in freq and len(freq)>0:
               secondhighest.append(rep[freq.index(max(freq))])
               rep.remove(rep[freq.index(max(freq))])
               freq.remove(max(freq))
            if len(secondhighest)==1:
                print(abs(high-lower))
            else:
                print(abs(high-max(secondhighest)))
        else:
            print(abs(max(highest)-min(highest)))
        
            
            
        
       
                
                
                
        
    
    
    
