# binary search
arr = [1,2,3,4,5,6,19,20,234,245]
target = 213

def binary_search(arr,target):
    l = 0
    r = len(arr)-1
    print('hi')
    while(l<=r):
        print("HI")
        mid = (l+r)//2
        print(arr[l:r+1])
        if(target>arr[mid]):
            l=mid+1
        elif(target<arr[mid]):
            r = mid-1
        elif(target==arr[mid]):
            l=r
            return True
    return False

print(binary_search(arr,target))


def binary_search_recursive(arr,target):
    if(len(arr)==1 and arr[0]==target):
        return True
    if(len(arr)==0):
        return False
    mid = len(arr)//2
    print(arr,mid,target)
    if(target>arr[mid]):
        arr = arr[mid+1:]
        ans = binary_search_recursive(arr,target)
    elif(target<arr[mid]):
        arr = arr[0:mid]
        ans = binary_search_recursive(arr,target)
    return ans


print(binary_search_recursive(arr,target))
