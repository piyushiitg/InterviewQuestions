

preorder = [40, 30, 35, 80, 100]

def canRepBST():
    global preorder
    s = []
    root = -1
    for i in range(len(preorder)-1):
   
        if preorder[i] < root:
            return False 
        while (s and s[-1] < preorder[i]):
            root = s[-1]
            s.pop()
        s.append(preorder[i])
    return True

print canRepBST()

