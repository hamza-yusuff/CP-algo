n=int(input())
res=1
for i in range(1,n+1):
	res=res*i
if len(str(res))<=4:
	print(res)
else:
	res=str(res)
	print(res[-4:])
