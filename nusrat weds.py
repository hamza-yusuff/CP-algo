test=int(input())
if test>1:
    
    array=list(map(int,input().split()))
    if len(array)==len(set(array)):
        print('Sorry Kadzz!')
    else:
        scores=list(map(lambda x:array.count(x)	, set(array)))
        if 1 in scores:
            hell=list(set(array))
            print(hell[scores.index(1)])
            print('Nusrat weds Kadzz!')
        else:
            print('Sorry Kadzz!')
else:
    if test==1:
        x=int(input())
        print('Sorry Kadzz!')
    else:
        print('Sorry Kadzz!')
		
	
