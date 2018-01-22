
inorder = ["D", "B", "E", "A", "F", "C"]
preorder = ["A", "B", "D", "E", "C", "F"]
preorderIndex = 0
class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def find_element(inorder, inorderStart, inorderEnd, key):
    while inorderStart <= inorderEnd:
        if inorder[inorderStart] == key:
            return inorderStart
        inorderStart += 1
    return -1   
def buildTree(inorder, preorder, inorderStart, inorderEnd):

    global preorderIndex
    if inorderStart > inorderEnd:
        return None

    data = preorder[preorderIndex]
    print data
    newNode = Node(data)

    preorderIndex += 1

    if inorderStart == inorderEnd:
        return newNode

    inorderIndex = find_element(inorder, inorderStart, inorderEnd, newNode.key)
    if inorderIndex == -1:
        return None

    newNode.left = buildTree(inorder, preorder, inorderStart, inorderIndex -1)
    newNode.right = buildTree(inorder, preorder, inorderIndex+1, inorderEnd)
    return newNode

def t_inorder(root):
    if root:
        t_inorder(root.left)
        print root.key
        t_inorder(root.right)


def t_preorder(root):
    if root:
        print root.key
        t_preorder(root.left)
        t_preorder(root.right)

newroot = buildTree(inorder, preorder, 0, len(inorder)-1)
print "inorder"
t_inorder(newroot)
print "preorder"
t_preorder(newroot)
