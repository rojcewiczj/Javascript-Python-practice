class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    

l1 = LinkedList(Node(0))
l2 = LinkedList(Node(1))

l1.head.next = Node(3)
l1.head.next.next = Node(5)

l2.head.next = Node(2)
l2.head.next.next = Node(9)


def merge(l1 , l2):
    if l1.head == None:
        return l2
    if l2.head == None:
        return l1
    
    if(l1.head.value < l2.head.value):
        current = l2.head
        to_return = l1.head
    else:
        current = l1.head
        to_return = l2.head
    
    while current != None:
        insert(current.value, to_return)
        current = current.next

    return to_return


def insert(value, to_return):
    new_node = Node(value)
    current = to_return
    while current.next != None:
        if(value < current.next.value):
            temp = current.next
            current.next = new_node
            new_node.next = temp
            return
        current = current.next
    
    current.next = new_node
    
merge(l1, l2)

print(l1.head.next.next.next.next.next.value)