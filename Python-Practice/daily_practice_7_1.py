class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, new_node):
    new_node = Node(new_node)
    print(root.data)
    if new_node.data < root.data:
        if root.left is None:
            root.left = new_node
        else:
            insert(root.left, new_node)
    elif new_node.data > root.data:
        if root.right is None:
            root.right = new_node
        else:
            insert(root.right, new_node)
