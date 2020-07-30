flipper=[[r for r in range(1,3)]for c in range(2)]
flipper[1][0]=3
flipper[1][1]=4
def output():
    for c in range(2):
       for r in range(2):
          print(flipper[c][r],end=' ')
       print('\n')
def vertical():
    for k in range(2):
        res=flipper[k][0]
        flipper[k][0]=flipper[k][1]
        flipper[k][1]=res
def horizontal():
    for s in range(2):
        res=flipper[0][s]
        flipper[0][s]=flipper[1][s]
        flipper[1][s]=res
string=input()
for i in range(len(string)):
    if string[i]=='H':
        horizontal()
    else:
        vertical()
output()
