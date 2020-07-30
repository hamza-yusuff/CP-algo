num=int(input())
for i in range(1,num+1):
	numbers=list(map(int,input().split()))
	res=numbers[0]+numbers[1]
	print('Case #{}:{}'.format(i,res))
	
