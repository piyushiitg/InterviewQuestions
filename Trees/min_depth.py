
import tree


root = tree.create_tree()

def min_height(root):
    if root is None:
        return 0

    if root.left == None and root.right == None:
        return 1
    return min(min_height(root.left), min_height(root.right)) + 1

print min_height(root)
