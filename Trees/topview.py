import tree

root = tree.create_tree()
d = {}
def bottom_view(root, column):
    global d
    if root:
        if d.has_key(column):
            pass
        else: 
            d[column] = root.key
        bottom_view(root.left, column-1)   
        bottom_view(root.right, column+1)

bottom_view(root, 0)
print d.values()
