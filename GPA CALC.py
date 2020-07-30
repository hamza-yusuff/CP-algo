num=int(input())
for i in range(num):
	number=int(input())
	score=[]
	for k in range(number):
		score.append(float(input()))
	gpa=(sum(score))/number
	print('Case {}:'.format(i+1),round(gpa,3))
