class Node:
    def _init_(self):
        self.value = 1
        self.next = 1
        self.prev = 1
class Linked_list:
    def _init_(self):
        self.head = None
        
    def insert_head(self, inti):
        node = Node()
        node.value= inti
        self.head = node
        next_node = Node()
        self.head.next = next_node.value
        print(self.head.next)
    def insert(self, inti):
       node = Node()
       node.value = inti
       if self.head.next.value == 1:
           self.head.next = node
        

      
       
           

    
        




linkedL = Linked_list()
linkedL.insert_head(2)
linkedL.insert(3)
print(linkedL.head.value)

               
    
    
