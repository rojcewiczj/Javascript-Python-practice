class B_Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


first_node = B_Node(5)

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
   
    



insert(first_node, B_Node(2))
insert(first_node, B_Node(9))
insert(first_node, B_Node(7))
insert(first_node, B_Node(3))
insert(first_node, B_Node(1))


recursive_print(first_node)


    
            

