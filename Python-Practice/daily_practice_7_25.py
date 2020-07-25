
nodes = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]] 
swaps = [2, 4]

class bi_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root_node = bi_node(1)

def insert_left(root, value):
    new_node = bi_node(value)
    if root.left is None:
        root.left = new_node
    else:
        insert_left(root.left, value)

def insert_right (root, value):
    new_node = bi_node(value)
    if root.right is None:
        root.right = new_node
    else:
        insert_right(root.right, value)

for array in nodes:
    if array[0] != -1:
        insert_left(root_node, array[0])
    if array[1] != -1:
        insert_right(root_node, array[1])


def print_tree(root):
    queue = [root]
    while len(queue) > 0:
        latest = queue.pop(0)
        print(latest.value)
        if latest.left is not None:
            queue.append(latest.left)
        if latest.right is not None:
            queue.append(latest.right)

print_tree(root_node)







