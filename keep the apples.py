numb,eachb=input().split()
numb=int(numb)
eachb=int(eachb)
ith=list(map(int,input().split()))
total=sum(ith)
if total%eachb==0:
	print(total/eachb)
else:
	print(int(total/eachb)+1)
