string=input()
cyclic=list(input())
found=True
for i in range(len(cyclic)):
    first=cyclic.pop(0)
    cyclic.append(first)
    res=''.join(cyclic)
    if res in string:
        print('yes')
        found=False
        break
if found==True:
    print('no')
