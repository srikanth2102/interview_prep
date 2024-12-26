#heap sort

import heapq
sorted_arr = []
arr = [1,2,4,52,24,5,34,324,12,435,12243]
heapq.heapify(arr)
length = len(arr)
for i in range(length):
    sorted_arr.append(heapq.heappop(arr))
print(sorted_arr)

