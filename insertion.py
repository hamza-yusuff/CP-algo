def insertion(arr):
    num=len(arr)
    for i in range(1,num):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
            
    return arr
print(insertion([2,1,4,3,6,5]))
