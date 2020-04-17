# Definition for singly-linked list.
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
    def delete(self, position):
        if self.head == None:
            return
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
            
        for i in range(position -1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next

        temp.next = None

        temp.next = next


    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
LL.delete(0)
LL.printLL()