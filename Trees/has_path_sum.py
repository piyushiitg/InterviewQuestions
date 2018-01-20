import tree

root = tree.create_tree()

def hasPathSum(root, sumk):
    print sumk
    if root is None:
        return sumk == 0

    if sumk == 0:
       return True

    remaining_sum = sumk - root.key

    if ((root.left and root.right) or (not root.left and not root.right)):
        return hasPathSum(root.left, remaining_sum) or hasPathSum(root.right, remaining_sum)

    elif root.left:
        return hasPathSum(root.left, remaining_sum)
    else:
        return hasPathSum(root.right, remaining_sum)

print hasPathSum(root, 11)

