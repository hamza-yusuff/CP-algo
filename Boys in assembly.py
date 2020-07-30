num,rotation=map(int,input().split())
array=list(map(int,input().split()))
if num==rotation or rotation%num==0:
    print(array[0], array[num-1])
else:
    for i in range(rotation):
        last=array.pop(0)
        array.append(last)
    print(array[0],array[len(array)-1])
    
