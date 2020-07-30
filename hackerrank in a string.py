s=input()
w=list(set("hackerrank"))
new=list(set(list(s)))
w=''.join(w)
new=''.join(new)
if w in new:
    print("YES")
else:
    print("NO")
    
        
        
    
