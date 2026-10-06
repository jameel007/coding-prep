## Bubble Sort
def bubble_sort(arr):
    size = len(arr)
    counter=0
    print(f"The give input array is: {arr}")
    for j in range(0,size):
        print("-----Out of Inner loop--------")
        
        for i in range(0,(size-1)-j):
            if arr[i]> arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            print(f"The array is: {arr}:{counter}")
            counter+=1
lst = [64, 34, 25, 12, 22, 11, 90] ##[1000,12,11,34,90,22,80,25,100,60,81]
result = bubble_sort(lst)