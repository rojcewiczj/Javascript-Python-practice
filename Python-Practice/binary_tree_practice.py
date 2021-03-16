class B_Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


first_node = B_Node(1)

def insert(root, node):
    if node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

def iterative_print(root):
    stack = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop(-1)
        print(current.data)
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)


def recursive_print(root):
    if root:
        if root.left is not None:
            recursive_print(root.left)
        print(root.data)
        if root.right is not None:
            recursive_print(root.right)
    
    

def breathFirst(root):
    queue = [root] # Node(1)                                                                                                      
    results = []                                                                                              
    while len(queue) > 0: 
        for node in queue:                                                   
            print(node.data)
        current = queue.pop(0)
        print("current value: ", current.data)
        results.append(current.data)
        if current.left != None:
            queue.append(current.left)
        if current.right!= None:
            queue.append(current.right)
    print(results)

first_node.left = B_Node(2)
first_node.left.right = B_Node(3)
first_node.right = B_Node(4)
first_node.right.left = B_Node(5)

breathFirst(first_node)


    
            

