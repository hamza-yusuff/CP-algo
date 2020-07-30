brackets=list(input())
first=brackets.count('(')
last=brackets.count(')')
if brackets[0]==')'or brackets[len(brackets)-1]=='(':
	print('No')
else:
	if first==last:
		print('Yes')
	else:
		print('No')
