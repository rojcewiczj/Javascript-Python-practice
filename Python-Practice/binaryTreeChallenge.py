class TreeNode:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.data == None:
            self.data = value
        elif self.data != None:
            if value < self.data:
                if self.left == None:
                    self.left = TreeNode(value)
                else:
                    self.left.insert(value)
            if value > self.data:
                if self.right == None:
                    self.right = TreeNode(value)
                else:
                    self.right.insert(value)
    
                   


new_tree = TreeNode(7)
new_tree.insert(4)
new_tree.insert(9)
new_tree.insert(6)
new_tree.insert(10)
print(new_tree.right.right.data)

                


