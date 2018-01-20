import tree

root = tree.create_tree()

max_value = 0
no_of_leaves = 0
def BFS(root):
    global max_value, no_of_leaves
    q = []
    
    if root is None:
        return
    
    q.append(root)

    while(q):
        node = q.pop(0)
        print node.key
        if max_value < node.key:
            max_value = node.key
        
        if node.left:
            q.append(node.left)

        if node.right:
            q.append(node.right)
        if node.left is None and node.right is None:
            no_of_leaves += 1
        
def BFS_reverse(root):
    if root is None:
        return 

    queue = []
    stack = []

    queue.append(root)
    while queue:
        node = queue.pop(0)
        stack.append(node)

        if node.right:
            queue.append(node.right)

        if node.left:
            queue.append(node.left)

    for i in range(len(stack)-1, -1, -1):
        print stack[i].key

        
print "BFS"
BFS(root)
print "BFS Reverse **"
BFS_reverse(root)
print "Max Value is"
print max_value
print "No of leaves"
print no_of_leaves

