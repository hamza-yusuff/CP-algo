n=int(input())
s=1
if n==0:
	print(1)
else:
	for i in range(1,n+1):
		s=s*i
	print(s)
