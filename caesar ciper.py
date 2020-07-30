num=[i for i in range(65,91)]
shift=int(input())
entry=input()
sent=entry.split(' ')
new=[]
for i in range(len(sent)):
	word=sent[i].upper()
	word=list(word)
	for c in range(len(word)):
		value=ord(word[c])
		res=value-shift
		if res<65:
			sub=65-res
			add=91-sub
			word[c]=chr(add)
		else:
			word[c]=chr(res)
	sent[i]=''.join(word)
	sent[i]=sent[i].lower()
print(' '.join(sent))		
			
		
		
				   
