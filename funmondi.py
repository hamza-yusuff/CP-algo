num,q=map(int,input().split())
array=list(map(int,input().split()))
for i in range(q):
	dhukber,school=map(int,input().split())
	if dhukber==1:
		array[school-1]=array[school-1]-1
	if dhukber==2:
		array[school-1]=array[school-1]+1
	res=array[:]
	for k in res:
		if k<=0:res.remove(k)
	print(len(res))
