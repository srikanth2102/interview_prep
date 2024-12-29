#quick sort
arr = [-3,1,2,-4,523,23,-34,5]

def quick_sort(arr):

    if(len(arr)<=1):
        return arr

    pivot = arr[-1]
    left_arr  =[x for x in arr[:-1] if x<=pivot]
    right_arr = [x for x in arr[:-1] if x>pivot]

    print(left_arr)
    print(right_arr)

    left_arr = quick_sort(left_arr)
    right_arr = quick_sort(right_arr)

    return left_arr + [pivot] + right_arr
    
print(quick_sort(arr))
