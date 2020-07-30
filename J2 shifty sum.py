app=int(input())
shifty=int(input())
array=[str(app)+str(0)*i for i in range(0,shifty+1)]
print(sum(list(map(int,array))))
