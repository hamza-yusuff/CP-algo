x,y=map(int,input().split())
row=[[0 for c in range(x)]for r in range(y)]
for r in range(y):
    for c in range(x):
        print(row[r][c],end=' ')
    print('\n')
