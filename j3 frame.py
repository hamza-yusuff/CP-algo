test=int(input())
x=[]
y=[]
for i in range(test):
    answer=list(map(int,input().split(',')))
    x.append(answer[0])
    y.append(answer[1])
lowest_x=min(x)-1
highest_x=max(x)+1
lowest_y=min(y)-1
highest_y=max(y)+1
bottom=[str(lowest_x),str(lowest_y)]
top=[str(highest_x),str(highest_y)]
print(','.join(bottom))
print(','.join(top))
    
