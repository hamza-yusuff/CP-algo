def equal(stack1,stack2,stack3):
   while True:
        if sum(stack1)==sum(stack2)==sum(stack3):
            break
        length=[sum(stack1),sum(stack2),sum(stack3)]
        high=max(length)
        pos=length.index(high)
        if pos==0:
            stack1.pop()
        elif pos==1:
            stack2.pop()
        else:
            stack3.pop()

   return sum(stack1)


num=map(int,input().split())
stack1=list(map(int,input().split()))
stack2=list(map(int,input().split()))
stack3=list(map(int,input().split()))
if sum(stack1)==sum(stack2)==sum(stack3):
    print(sum(stack1))
else:
    print(equal(stack1[::-1],stack2[::-1],stack3[::-1]))

