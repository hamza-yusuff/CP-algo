num=int(input())
goat=[]
for i in range(num):
    string=input()
    alpha=string.count('a')
    if alpha%2!=0:
        string=string[:len(string)-1]
        if string.count('a')==0:
            string=string+'aa'
    goat.append(string)
highest=len(max(goat))
for x in range(num):
    print((int((highest-len(goat[x]))/2))*' '+goat[x])
