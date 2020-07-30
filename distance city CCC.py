
def distance(hell,i):
	new=[]
	hell.insert(i,0)
	first=hell[:i+1]
	second=hell[i:]
	if len(first)>1:
	   first=first[::-1]
	   for k in range(len(first)):
		    new.append(sum(first[:k+1]))
	   new=new[::-1]
	if len(second)>1:
	   for t in range(len(second)):
		    new.append(sum(second[:t+1]))
	return new
a,b,c,d=map(int,input().split())
for i in range(5):
    lamda=distance([a,b,c,d],i)
    if lamda.count(0)>1:
        lamda.remove(0)
    print(' '.join(list(map(str,lamda))))
