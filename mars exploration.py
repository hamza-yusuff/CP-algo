word=input()
rep=int(len(word)/3)
original="SOS"*rep
changed=0
for i in range(len(word)):
    if word[i]!=original[i]:
        changed=changed+1
print(changed)
