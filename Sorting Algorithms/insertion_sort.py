#insertion sort




arr = [52,24,5,34,324,12,435,12243,1,2,4]
for i in range(len(arr)):
    try:
        current = arr[i+1]
        for j in range(0,i+1):
            if(current<arr[j]):
                arr.pop(i+1)
                arr.insert(j,current)
                break;
    except IndexError:
        break;

print(arr)
