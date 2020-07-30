test=int(input())
for i in range(test):
	string=input()
	ucount=0
	lcount=0
	digit=0
	for w in string:
		if w.isupper()==True:
			ucount=ucount+1
		elif w.islower()==True:
			lcount=lcount+1
		elif w.isdigit()==True:
			digit=digit+1
	print('Case {}:'.format(i+1),min(ucount,lcount)+digit)
