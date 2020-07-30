for i in range(1,int(input())+1):
	total=0
	fail=0
	credit=0
	for k in range(int(input())):
		a,c=input().split()
		a=int(float(a))
		c=float(c)
		if a>=80 and a<=100:
			total=total+4.00*c
		elif a>=75 and a<=79:
			total=total+3.75*c
		elif a>=70 and a<=74:
			total=total+3.50*c
		elif a>=65 and a<=69:
			total=total+3.25*c
		elif a>=60 and a<=64:
			total=total+3.00*c
		elif a>=55 and a<=59:
			total=total+2.75*c
		elif a>=50 and a<=54:
			total=total+2.50*c
		elif a>=45 and a<=49:
			total=total+2.25*c
		elif a>=40 and a<=44:
			total=total+2.00*c
		else:
			fail=fail+1
		credit=credit+c
	if fail==0:
		res=total/credit
		print("Case {}: {:.2f}".format(i,res))
	elif fail>0:
		print("Case {}: Sorry, you have failed in {} in courses!".format(i,fail))
		
		

			
