import tree

root = tree.create_tree()

def mirror(root):
    q = []
    if root is None:
        return None
    q.append(root)
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        node.left, node.right = node.right, node.left

def preorder(root):
    if root:
        print root.key
        preorder(root.left)
        preorder(root.right)

def check_mirror(root1, root2):
    if root1 == None and root2 == None:
        return True
    
    if root1 == None or root2 == None:
        print "FFF"
        return False

    
    if root1.key != root2.key:
        print "DDAAA", root1.key, root2.key
        return False

    return check_mirror(root1.left, root2.right) and check_mirror(root1.right, root2.left)
  
print "before Mirror"
root1 = root
preorder(root)
mirror(root)
root2  = root
print "After Mirror"
preorder(root2)
print "Check mirror"
print check_mirror(root1, root2)

