test=int(input())
for i in range(1,test+1):
	currentcost=sum(list(map(int,input().split())))
	budget=int(input())
	nextmonth=sum(list(map(int,input().split())))
	if currentcost<=budget:
		res=nextmonth-(budget-currentcost)
		if res<0: res=0
		print('Case {}:'.format(i),res)
	else:
		res=(currentcost-budget)+nextmonth
		print('Case {}:'.format(i),res)
		
