def binary_search(input_array, value):
    l=len(input_array)
    r=1
    while r<=l:
        middle=(l+(r-1))/2
        if input_array[int(middle)-1]==value:
            return int(middle)-1
            break 
        if input_array[int(middle)-1]<value:
            r=middle+1
        else:
            l=middle-1

    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
