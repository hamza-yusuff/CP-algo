num=int(input())
if num==0:
    print('0')
else:
    binary=list(bin(num))
    binary.remove('b')
    new=list(map(int,binary))
    new=list(map(lambda x:x*-1,new))
    new.sort()
    f=new.index(0)
    new=new[:f]
    new=list(map(lambda x:x*x,new))
    new=list(map(str,new))
    print(int(''.join(new),2))




