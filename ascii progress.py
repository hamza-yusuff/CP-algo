num=input()
x=float(num)
out=int(x)
work=(int(int(x)/10))*10

if work==0:
    print('[..........]',str(out)+'%')
elif work==100:
    print('[++++++++++]',str(out)+'%')
else:
    work=str(work)
    first=int(work[0])
    string='['+first*'+'+(10-first)*'.'+']'
    print(string,str(out)+'%')


