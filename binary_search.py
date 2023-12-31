def binary_search(arr,t):
    left,right=0,len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]==t:
            return True
        elif arr[mid]<t:
            left=mid+1
        else:
            right=mid-1
    return -1

print(binary_search([1,2,3,4,5,6,7,8],2))