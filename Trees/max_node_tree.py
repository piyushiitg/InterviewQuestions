import tree
root = tree.create_tree()

max_value = None

def max_node(root):
    global max_value
    if root:
        max_node(root.left)
        if max_value == None:
            max_value = root.key
        else:
            if max_value < root.key:
                max_value = root.key
        max_node(root.right)
   

max_node(root)
print max_value
