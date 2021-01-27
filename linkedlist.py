class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None


    def Insert(self, value):
        new_node = Node(value)
        if(self.head == None):
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
        

    def print(self):
        current = self.head

        while(current.next != None):
            print(current.value)
            current = current.next
        
        print(current.value)

    
    def remove(self, k):
        if(self.head.value == k):
            self.head = self.head.next
        current = self.head
        while(current.next != None):
            while(current.next != None and current.next.value == k):
                current.next = current.next.next
        
            if current.next != None:
                current = current.next
           
    
    def special_insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        elif value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while(current.next != None):
                if current.next.value > value:
                    old_next = current.next
                    current.next = new_node
                    new_node.next = old_next
                    break
                current = current.next
            
            current.next = new_node
            
            
            



        
            
            

        
Listy = LinkedList()

list_of_nums = [2,5,4,1,9,3]


for num in list_of_nums:
    Listy.special_insert(num)



Listy.print()

value = 5


     



