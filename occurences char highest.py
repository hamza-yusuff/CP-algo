num=input()
chars=[0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    x=num.count(str(chars[i]))
    chars[i]=x
highest=max(chars)
t=[]
for i in range(10):
    if highest==chars[i]:
        t.append(i)
if len(t)>=2:
    print(min(t))
else:
    print(t[0])
