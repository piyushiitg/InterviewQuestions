import tree

root = tree.create_tree()


def tree_size(root):
    if root is None:
        return 0

    return 1 + tree_size(root.left) + tree_size(root.right)


print tree_size(root)
