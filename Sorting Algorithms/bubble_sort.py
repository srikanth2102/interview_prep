#bubble sort

'''
compare the adjacent elements and then swap if right is greater
'''
arr = [23,22,324,212,353,12434,243,1,5,9]
for i in range(len(arr)):
    for j in range(len(arr)):
        try:
            if(arr[j+1]<arr[j]):
                temp = arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
        except IndexError:
            break;
    print(arr)
print(arr)
