bus,work=map(int,input().split())
fan=list(map(int,input().split()))
fan=sorted(fan)
for i in range(1,work+1):
	print(fan[bus-i])
