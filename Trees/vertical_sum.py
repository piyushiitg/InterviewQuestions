import tree
from collections import OrderedDict
root = tree.create_tree()
d = OrderedDict()

def verticalSum(root, column):
    global d
    if root is None:
        return None

    verticalSum(root.left, column-1)
    if d.has_key(column):
        d[column] = d[column] + root.key
    else:
        d[column] = root.key

    verticalSum(root.right, column+1)


verticalSum(root, 0)
print d
