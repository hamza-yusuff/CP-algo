def compute(n):
	n=list(str(n))
	number=list(map(lambda x:n.count(x),set(n)))
	print(number)
	print(sum(number))
	print(max(n))
	if sum(number)==int(max(n)):
		return True
	else:
		return False
print(compute(1))
