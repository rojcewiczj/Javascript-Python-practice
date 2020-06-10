class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    


node = Node(1)
second_node = Node(2)
node.next = second_node


def insert(data , head):
    new_node = Node(data)
    if head.data > data:
        old_head = head
        new_head = new_node
        new_head.next = old_head
    print(new_head.data, new_head.next.data, new_head.next.next.data)

insert(0, node)