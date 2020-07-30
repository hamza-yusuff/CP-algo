num=int(input())
count=0
for i in range(2,num):
  for k in range(num,1,-1):
      if k*i<=num:
          count=count+1
