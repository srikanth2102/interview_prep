class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.val)

#        1
#     2    3
#   4  5  10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A.left)




#BFS
'''
giving the root of the tree as the input is enough
'''

print("BFS")
queue = [A]
while(queue):
    popped = queue.pop(0)
    if(popped):
        print(popped)
        queue.append(popped.left)
        queue.append(popped.right)

#BFS - recursive

def pre_order(A):
    
    if not A:
        return
    print(A)
    pre_order(A.left)
    pre_order(A.right)

def in_order(A):
    if not A:
        return

    in_order(A.left)
    print(A)
    in_order(A.right)


#DFS
'''
In Order traversal. Need to use stack
'''

print("DFS - In order")
stack = [A]
while(stack):
    popped = stack.pop()
    if(popped):
        print(popped)
        stack.append(popped.right)
        stack.append(popped.left)

        
print("DFS In-order")
in_order(A)
print("DFS Pre-order")
pre_order(A)
