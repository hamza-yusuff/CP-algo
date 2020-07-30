string=input()
first=['(','{','[']
second=[')','}',']']
c1=[0,0,0]
c2=[0,0,0]
fish=True
for i in range(len(string)):
    if string[i] in first:
        s=first.index(string[i])
        if i!=len(string)-1:
                    if string[i+1] in second:
                     c=second.index(string[i+1])
                     if c!=s:
                      print('No')
                      fish=False
                      break
        c1[s]=c1[s]+1
    elif string[i] in second:
        q=second.index(string[i])
        c2[q]=c2[q]+1
if string[0] not in second and string[len(string)-1] not in first and fish==True:
    if c1[1]==c2[1] and c1[0]==c2[0] and c1[2]==c2[2]:
        print('Yes')
    else:
        print('No')
elif fish==True:
    print('No')
            


        
