class Node():
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

def create_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    """
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.right = Node(10)
    root.left.left.left.right = Node(11)
    """
    a = """Your Tree is 
                                1

                      2                 3

                 4           5       6          7
        """

    b= """

              8      9   10     

                 11  
        """
    print a 
    return root

    
if __name__ == "__main__":
    root = create_tree()
