x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=int(input())
def find(x,y,z):
    for i in range(len(x)):
        res=z-x[i]
        if res in y:
            return True
            break
    else:
        return False
print(find(x,y,z))
