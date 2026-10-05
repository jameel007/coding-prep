## Linear Search  - meaning searching every element in the array.

def linear_search(arr,target):

    
    size = len(arr)
    for index in range(0,size):
        if arr[index] == target:
            return index
    return -1

lst = [0,10,20,25,60,320]
target =320

print(linear_search(lst,target))