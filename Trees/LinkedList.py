head = None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_node(data):
    global head
    newNode = Node(data)
    if head == None:
        head = newNode
        return
    temp = head
    while temp.next != None:
        temp = temp.next

    temp.next = newNode

def print_nodes():
    global head
    temp = head
    while temp != None:
        print temp.data
        temp = temp.next

for i in range(10):
    add_node(i)

print_nodes()
