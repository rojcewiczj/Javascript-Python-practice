class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.root = val
        self.left = left
        self.right = right
    def insert(self, value):
        if self.root == None:
            self.root = value
        elif self.root != None:
            pass