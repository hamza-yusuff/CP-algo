









n,q=map(int,input().split())
array=list(map(int,input().split()))
array.sort()
for i in range(q):
	f=list(map(int,input().split()))
	if f[0]==1:
		array=list(map(lambda x:x-f[1],array))
	else:
		if f[2]-f[1]<f[3] and f[2]!=f[1]:
			print(-1)
		else:    

			k=list(set(array[f[1]-1:f[2]]))
			
			

		    
			print(k[f[3]-1])
