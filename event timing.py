for i in range(1,int(input())+1):
	p,k,d=map(int,input().split())
	if round(k/d)==0:
		res=p+d
	else:
		res=p+d*(int(k/d)+1)
	print('Case {}:'.format(i),res)
