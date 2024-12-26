#selection sort
'''
logic:
traverse the unsorted array and get the smallest and set that to
that start of the unsorted array

assumption ---> max element in the arr is less than 10^5
'''

arr = [2,4,1,23,82,2094,23,245,234,132]
for i in range(len(arr)):
    min = (10**5)+1
    ind = i
    for j in range(i,len(arr)):
        if(arr[j]<min):
            min=arr[j]
            ind = j
    temp = arr[i]
    arr[i]=arr[ind]
    arr[ind]=temp
print(arr)
