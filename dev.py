def divisor(n):
	dev=[]
	for k  in range(1,n+1):
		if n%k==0:
			dev.append(k)
	return dev
print(divisor(63))
