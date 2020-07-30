num=int(input())
def check(string):
    new=list(string)
    length=len(new)
    if new.count('N')!=0:
        Ncount=new.count('N')
        length=length-Ncount
    if new.count('W')!=0:
        length=length-new.count('W')
    if new.count('D')!=0:
        length=length-new.count('D')
   
    if length<6 and length>1:
        print(length,'BALLS')
    elif length==1:
        print('1 BALL')
    else:
        inover=length%6
        if length==6:
            print('1 OVER')
        else:
            overs=(length-inover)/6
            if inover==1 and overs==1:
                print('1 OVER 1 BALL')
            elif overs==1 and inover>1:
                print('1 OVER',int(inover),'BALLS')
            else:
                if overs>1 and inover==1:
                    print(int(overs),'OVERS 1 BALL')
                elif overs>1 and inover==0:
                    print(int(overs),'OVERS')
                else:
                    print(int(overs), 'OVERS',int(inover),'BALLS')
            
for i in range(num):
    s=input()
    check(s)
