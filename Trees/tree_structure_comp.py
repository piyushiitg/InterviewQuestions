import tree

root1 = tree.create_tree()
root2 = tree.create_tree()

def AreStructurullySameTree(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 == None or root2 == None:
        return False

    return AreStructurullySameTree(root1.left, root2.left) and AreStructurullySameTree(root1.right, root2.right)


print AreStructurullySameTree(root1, root2)
