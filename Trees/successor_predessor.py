

import tree

root = tree.create_tree()

last_value = None
def preorder_successor(root, data, flag):
    global last_value
    if root is None:
        return

    if flag == 1 and last_value is None:
        print root.key
        last_value = root.key
        flag = 0
        
    if root.key == data:
        flag = 1
    preorder_successor(root.left, data, flag)
    preorder_successor(root.right, data, flag)

def inorder_successor(root, data):
    global last_value
    if root is None:
        return

    inorder_successor(root.left, data)
    if last_value == data:
        print root.key

    last_value = root.key
    inorder_successor(root.right, data)


preorder_successor(root, 3, 0)
flag = 0
last_value = None
inorder_successor(root, 4)
