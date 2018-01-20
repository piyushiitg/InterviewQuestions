
import tree

root = tree.create_tree()
path = []
max_value = None
no_of_leaves = 0
#Print Path using DFS
def dfs(root, path):
    global max_value, no_of_leaves
    if root is None:
        return

    if max_value is None:
        max_value = root.key

    if max_value < root.key:
        max_value = root.key

    path.append(root.key)
    if root.left == None and root.right == None:
        print path
        no_of_leaves = no_of_leaves + 1

    if root.left != None:
        dfs(root.left, path) 
    if root.right != None:
        dfs(root.right, path)
     
    path.pop()


dfs(root, path)
print "Max Value", max_value    
print "No_of_leaves", no_of_leaves
