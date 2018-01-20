import tree


def height(root):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return 1

    return max(height(root.left), height(root.right)) + 1

if __name__ == "__main__":
    root = tree.create_tree()
    print "height of tree"
    print height(root)
