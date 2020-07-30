
def add(x,y):
    answer=[]
    summation=0
    carry=0
    for i in range(len(x)-1,-1,-1):
        res=int(x[i])+int(y[i])+carry
        if res>9 and i!=0:
            carry=1
            answer.append(res-10)
        else:
            carry=0
            answer.append(res)
    answer=answer[::-1]
    answer=list(map(str,answer))
    output=''.join(answer)
    return output
def addbig(x,y):
    actual=len(x)
    x=[0]*(len(y)-len(x))+x
    answer=[]
    summation=0
    carry=0
    for i in range(len(x)-1,-1,-1):
        res=int(x[i])+int(y[i])+carry
        if res>9 and i!=0:
            carry=1
            answer.append(res-10)
        else:
            carry=0
            answer.append(res)
    answer=answer[::-1]
    answer=list(map(str,answer))
    output=''.join(answer)
    return output

num=int(input())
for k in range(num):
    first,second=input().split()
    first=list(first)
    second=list(second)
    if len(first)==len(second):
        print('Case #{}:'.format(k+1),add(first,second))
    elif len(first)>len(second):
        print('Case #{}:'.format(k+1),addbig(second,first))
    else:
        print('Case #{}:'.format(k+1),addbig(first,second))
