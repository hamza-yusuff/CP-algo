season=int(input())
swift=list(map(int,input().split()))
sem=list(map(int,input().split()))
rswif=0
rsem=0
k=[]
for i in range(len(swift)):
    rswif=swift[i]+rswif
    rsem=sem[i]+rsem
    if rswif==rsem:
        k.append(i+1)
if len(k)==0:
    print(0)
else:
    print(max(k))
