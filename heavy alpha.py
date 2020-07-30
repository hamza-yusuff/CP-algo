test=int(input())
for i in range(test):
    string=input()
    num=['#']*len(string)
    num[0]=string[0]
    j=0
    for k in range(len(string)):
        while j<len(string)-1:
            if string[j].upper()==string[j+1].upper():
                j=j+1
                pass
            else:
                j=j+1
                num[j]=string[j]
                break
        k=j
    print(''.join(num))
            
        
