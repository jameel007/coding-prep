## Binary Search   - meaning diving the search bi...half.
## ** Can only be performed on the sorted array i.e ascending or descending order **
def binary_search(arr,target):
   
    size = len(lst)
    start = 0
    end = size - 1
   ## print(len(arr))
    while (start<=end):
        mid = (end + start)//2
       
        if arr[mid] == target:
            return mid       
        
        elif arr[mid]>target:
            end = mid -1     
        
        elif arr[mid]<target:
            start= mid + 1 
    return -1

lst = [10,20,30,40,50,60,70,100]
target = 50
result = binary_search(lst,target)
print(result)