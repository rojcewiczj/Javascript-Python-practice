def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedList()
    new_node.data = data
    inc = 0
    if head.next is not None:
        current = head
        while current.next is not None:
            current = current.next
            if inc == (position - 2):
                break
            inc += 1
    to_shift = current.next
    current.next = new_node
    current.next.next = to_shift
    if head.next is not None:
        current = head
        return current
        while current.next is not None:
            current = current.next
            return current