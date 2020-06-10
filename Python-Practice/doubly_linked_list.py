# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
# def sortedInsert(head, data):
#     new_node = DoublyLinkedListNode(data)
    
#     if head.next is not None:
#         if head.data > data:
#             old_head = head
#             head = new_node
#             head.next = old_head
#             old_head.prev = head
#             print(old_head.prev.data, old_head.next.data)
#         current = head.next
#         while current.next is not None:
#             if current.next.data > data:
#                 current = current
#                 lower = current
#                 to_switch = current.next
#                 current.next = new_node
#                 new_node.prev = lower
#                 new_node.next = to_switch
#                 to_switch.prev = new_node
#                 break
#             current = current.next
            

#     if head.next is not None:
#         current = head.next
#         return head
#         while current.next is not None:
#             if current == head.next:
#                 return current
#             current = current.next
#             return current

# array = ["one", "two", "three"]
# new_array = array


# print(new_array)
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

        

    








 

            