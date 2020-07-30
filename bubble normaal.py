def bubble(array):
    size=len(array)
    for i in range(size):
        for j in range(size-1-i):
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    return array
print(bubble([1,5,3,9,0,2]))
                
