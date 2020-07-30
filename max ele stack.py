# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
stack=[0]*n
tail=0
for i  in range(n):
    s=input()
    if s[0]==1:
        stack[tail]=s[1]
        tail+=1
    elif s[0]==2:
        tail-=1
    elif s[0]==3:
        print(max(stack[:tail]))
