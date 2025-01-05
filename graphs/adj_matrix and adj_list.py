#Edge list
n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]



# convert the edge list to adjacency matrix
adj_matrix = [[0]*n for i in range(n)]

for i,j in A:
    adj_matrix[i][j] = 1

    #if the graph is undirected (both ways)
    adj_matrix[j][i] = 1

print(adj_matrix)


#convert edge list to adjacency list (hashmap basically)
adj_list = {}
for i,j in A:
    if(i in adj_list):
        adj_list[i].append(j)
    else:
        adj_list[i] = [j]
print(adj_list)
