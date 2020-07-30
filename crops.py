def show(n):
    for k in range(8):
        for t in range(8):
            print(n[k][t],end=' ')
        print('\n')
x,y=input().split()
x=int(x)
y=int(y)
num=[[True for c in range(x+2)]for i in range(y+2)]
for i in range(1,y+1):
    string=' '+input()+' '
    for c in range(1,x+1):
        if string[c]=='*':num[i][c]='False'
count=0
for i in range(1,y+1):
    for c in range(1,x+1):
        if num[i][c]==True and num[i+1][c]==True and num[i-1][c]==True and num[i][c+1]==True and num[i][c-1]==True:
            count=count+1
print(count)
