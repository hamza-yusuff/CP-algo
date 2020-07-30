def find(s):
	global cans
	return cans.count(s)
num,tp=map(int,input().split())
cans=list(map(int,input().split()))
cans=sorted(cans)
if list(set(cans))==cans:
	print(cans[0])
else:
	numbers=list(map(find,[i for i in range(1,tp+1)]))
	print(cans[cans.index(max(numbers))])
