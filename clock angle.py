h,m=input().split()
h=int(h)
m=int(m)
minute=6*m
if h>=6:
	hour=(12-h)*30-((m/60)*30)
	hour=360-hour
else:
	hour=h*30+((m/60)*30)
if hour>minute:
    difference1=hour-minute
else:
    difference1=minute-hour
difference2=360-difference1
if difference1>difference2:
	print('{:.7f}'.format(difference2))
else:
	print('{:.7f}'.format(difference1))
