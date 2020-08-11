def reverse(head):

    stack = []
    current = head.next
    stack.append(head)

    while current is not None:
        stack.append(current)
        current = current.next
    print(stack[-1].data)
    node = stack.pop(-1)
    head = node
    head.next = head.prev
    head.prev = head.next
   
    while len(stack) > 0:
        node = stack.pop(-1)
        node.next = node.prev
        node.prev = node.next

    return head
    