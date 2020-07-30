string=input()
string=list(string)
cur='({['
pur=')}]'
s=True
if string[0] not in cur or string[len(string)-1] not in pur:
    print('No')
    print('1')
else:
    paren1=string.count('(')
    paren2=string.count(')')
    curly1=string.count('{')
    curly2=string.count('}')
    square1=string.count('[')
    square2=string.count(']')
    for i in range(len(string)-1):
            if string[i] in cur:
                if string[i+1] in pur:
                    print('No')
                    s=False
                    break
    if paren1==paren2 and curly1==curly2 and square1==square2 and s==True:
        print('Yes')
    elif s==True:
        print('No')
    
    
