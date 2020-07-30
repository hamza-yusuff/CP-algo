num=int(input())
for i in range(num):
	x,y,nth=input().split()
	diff=int(y)-int(x)
	n=((int(nth)-int(x))/diff)+1
	res=(n/2)*(2*int(x)+(n-1)*diff)
	print(res)
	
