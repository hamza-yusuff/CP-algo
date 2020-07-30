import math
def binary(num):
    d=round(math.log(num,2))
    res=num
    i=d
    string=''
    while i>=0:
        if res<2**i:
            string=string+'0'
        else:
            string=string+'1'
            res=res-2**i
        i=i-1
    return string
print(binary(72))
def decimal(biner):
    biner=list(biner)
    biner=biner[::-1]
    summation=0
    for k in range(len(biner)):
        if biner[k]=='1':
            summation=summation+2**k
    return summation
print(decimal(binary(72)))
        
