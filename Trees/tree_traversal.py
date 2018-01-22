import tree
max_height = 0

def preorder(root):
    if root:
        print root.key
        preorder(root.left)
        preorder(root.right)

def preorder_non_recursive(root):
    s = []
    if root is None:
        return None

    while True:
        while root:
            print root.key
            s.append(root)
            root = root.left
        if not s:
            break
        root = s.pop()
        root = root.right

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.key

def inorder(root):
    if root:
        inorder(root.left)
        print root.key
        inorder(root.right)

ksum = 0
def rev_inorder(root):
    global ksum
    if root is None:
        return
    rev_inorder(root.right)
    ksum = root.key + ksum
    print "-----", root.key, ksum
    root.key =  ksum
    rev_inorder(root.left)

root = tree.create_tree()

"""
print "PreOrder ****"
preorder(root)
preorder_non_recursive(root)
"""
print "InOrder ****"
inorder(root)
"""
print "PostOrder ****"
postorder(root)
"""
print "Reverse Inorder"
ksum=0
rev_inorder(root)
inorder(root)
