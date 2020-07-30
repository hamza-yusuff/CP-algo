p=int(input())
n=int(input())
r=int(input())
day=0
add=0
while True:
    add+=n
    n=(n*r)
    if add>p:
        break
    else:
        day+=1
print(day)
