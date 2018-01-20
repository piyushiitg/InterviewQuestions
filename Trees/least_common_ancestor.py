# O(n) solution to find LCS of two given values n1 and n2
import tree

# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path 
# exists otherwise false
def findPath( root, path, k):
    print "****** Searching for k %s" %k
    # Baes Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.key)
    print path
    # See if the k is same as root's key
    if root.key == k :
        print "Root Key is %s" %root.key
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
	(root.right!= None and findPath(root.right, path, k))):
	return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
	
    path.pop()
    print path
    return False

# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):
    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1 
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    print path1, path2
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
	    break
	i += 1
    print i, path1[i]
    return path1[i-1]


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
print "LCA(4, 5) = %d" %(findLCA(root, 4, 5,))
#print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
#print "LCA(3, 4) = %d" %(findLCA(root,3,4))
#print "LCA(2, 4) = %d" %(findLCA(root,2, 4))

