string=input()
w=string.upper()
vowel=['A','E','I','O','U']
count=0
for i in range(len(w)):
	if w[i] in vowel:
		count=count+1
print(count)
