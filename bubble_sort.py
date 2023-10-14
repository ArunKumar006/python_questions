def bubble_sort(arr):
    n=len(arr)
    sorted=False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                sorted=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if not sorted:
            return""
arr=[1,2,12,4,75,23,0,5,27]
bubble_sort(arr)
print(arr)

