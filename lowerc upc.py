def checkl(word):
	count=0
	for w in word:
		if ord(w)>=97 and ord(w)<=122:
			count=count+1
	return count
def checku(word):
	count=0
	for w in word:
		if ord(w)>=65 and ord(w)<=90:
			count=count+1
	return count

test=int(input())
for i in range(test):
	string=input()
	if string.isupper()==True or string.islower()==True:
		print('Case {}:'.format(i+1),'0')
	else:
		countl=checkl(string)
		countu=checku(string)
		print('Case {}:'.format(i+1),min(len(countl),len(countu)))
