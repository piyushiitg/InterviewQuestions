import tree

root = tree.create_tree()

max_sum = 0
def max_path_sum(root):
    global max_sum, prev_sum
    if root is None:
        return 0

    l = max_path_sum(root.left)
    r = max_path_sum(root.right)
    max_single = max(max(l, r) + root.key, root.key)

    max_top = max(max_single, l+r+root.key)
    
    max_sum = max(max_top, max_sum)
    return max_single    


max_path_sum(root)
print max_sum
