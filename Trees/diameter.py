import tree
import height
root = tree.create_tree()

def diameter(root):
    if root is None:
        return 0
    lheight = height.height(root.left)
    rheight = height.height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max((lheight+rheight+1), max(ldiameter, rdiameter))

print diameter(root)
