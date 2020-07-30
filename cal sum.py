test=int(input())
for i in range(test):
	num=int(input())
	if num%2==0:
		res=num/2
		print(int(res*1+res*-2))
	else:
		res1=(num+1)/2
		res2=(num-1)/2
		print(res1*1+res2*-2)
