class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None
class linked_list:
    def __init__(self):
        self.head = node()
        self.tail = node()
    
    def insert(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total +=1
            curr = curr.next
        return total
    
    def delete(self, data):
        curr = self.head
        while curr.next != None:
            if curr.next.data == data:
                curr.next = None
            else:
                curr = curr.next
    def find(self, data):
        curr = self.head
        while curr.next != None:
            if curr.next.data == data:
                print("prev : ", curr.next.prev.data, " curr : ", curr.next.data, " next : ", curr.next.next.data)
            curr = curr.next
    
    def reverse(self):
        curr = self.head
        to_reverse = []
        while curr.next != None:
            curr = curr.next
            if curr.prev != self.head and curr.next != None:
               to_reverse.append(curr)
        
        print(to_reverse[0].data)
 
    

                
           

        


            
            
       

        

my_list = linked_list()
my_list.insert(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.reverse()




        