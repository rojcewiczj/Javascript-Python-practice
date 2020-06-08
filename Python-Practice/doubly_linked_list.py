# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    
    if head.next is not None:
        if head.data > data:
            old_head = head
            head = new_node
            head.next = old_head
            old_head.prev = head
            print(old_head.prev.data, old_head.next.data)
        current = head.next
        while current.next is not None:
            if current.next.data > data:
                current = current
                lower = current
                to_switch = current.next
                current.next = new_node
                new_node.prev = lower
                new_node.next = to_switch
                to_switch.prev = new_node
                break
            current = current.next
            

    if head.next is not None:
        current = head.next
        return head
        while current.next is not None:
            if current == head.next:
                return current
            current = current.next
            return current
            