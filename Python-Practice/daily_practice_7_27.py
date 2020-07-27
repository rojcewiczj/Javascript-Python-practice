class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        print(l1)
        print(l2)
        
        first_list = []
        second_list = []
        total_list = []
        
        def get_list (node, listy):
            if node.val is not None:
                listy.append(node.val)
                while node.next is not None:
                    listy.append(node.next.val)
                    node = node.next
            
      
                    
        get_list(l1, first_list)
        get_list(l2, second_list)
        
        first_list_rev = list(reversed(first_list))
        second_list_rev = list(reversed(second_list))
     
        
        carry = 0 
        total = ListNode()
        inc = 0
        
        def create_total(root, inc ,carry):
            
            if inc < len(first_list_rev):
                root.val = first_list_rev[inc] + second_list_rev[inc] + carry
                if inc < len(first_list_rev) -1:
                    root.next = ListNode()
                carry = 0
                if len(str(root.val)) > 1:
                    carry = int(str(root.val)[0])
                    root.val = int(str(root.val)[1])
                
                create_total(root.next, inc + 1, carry)
                
            
        create_total(total, inc, carry)
        
        get_list(total, total_list)
        total_reversed = list(reversed(total_list))

        
        print(first_list_rev)
        print(second_list_rev)
        print(total_reversed)
        return total
        