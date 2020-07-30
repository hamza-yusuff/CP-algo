null=input()
num=list(null)
if len(num)<=3:
	print(null)
else:
    if len(num)%3==1 and len(num)!=0:
	    for i in range(1,len(num),4):
		    num.insert(i,',')
    elif len(num)%3==2 and len(num)!=0:
	    for i in range(2,len(num),4):
		    num.insert(i,',')
    elif len(num)%3==0 and len(num)!=0:
	    for i in range(3,len(num),4):
		    num.insert(i,',')
    print(''.join(num))


