mines=0
while True:
	
	try:
		string=input()
		mines=mines+string.count('m')
	except:
		break
print(mines)	
