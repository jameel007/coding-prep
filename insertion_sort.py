


def insertion_sort(arr):

    size = len(arr)
    
    for j in range(1,size):
        currentcard = arr[j]
        currentposition = j -1

        while currentposition >= 0:        
            if arr[currentposition]< currentcard:
                break
            else:
                arr[currentposition+1] = arr[currentposition]
                currentposition-=1
            arr[currentposition+1] = currentcard
        print(arr)
    print(arr)
lst = [12,25,11,34,90,10,0]
      
insertion_sort(lst)

"""  Insertion Sort
1. Compare one unsorted element with another beside it and then if lesser move it to left
2. Then compare the third with sorted arrays and insert inbetween if necessary like in cards.
3. 
"""