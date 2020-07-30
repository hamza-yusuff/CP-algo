num=int(input())
for i in range(num):
	nth=int(input())
	total=(nth/2)*(2*1+(nth-1)*2)
	print('Case {}:'.format(i+1),int(total))
