score=0
for i in range(1,4):
    x=int(input())
    score=x*i+score
if score>=10:
    print('happy')
else:
    print('sad')
