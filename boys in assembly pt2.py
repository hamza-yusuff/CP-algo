num,rotation=map(int,input().split())
array=list(map(int,input().split()))
if num==rotation or rotation%num==0 or rotation==0:
    print(array[0], array[num-1])
else:
    r=rotation%num
    print(array[int(r)],array[int(r)-1])
    
