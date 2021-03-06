class MyQueue:

    def __init__(self):
        self.left = []
        self.right = []
        
    
        

    def push(self, x: int) -> None:
        self.left.append(x)
        
        
        
        

    def pop(self) -> int:
        while len(self.left) > 0:
            self.right.append(self.left.pop())
        
        to_return = self.right.pop()
        while len(self.right) > 0:
            self.left.append(self.right.pop())
        return to_return

    def peek(self) -> int:
        return self.left[0]
        

    def empty(self) -> bool:
        if len(self.left) == 0 and len(self.right) == 0:
            return True
        else:
            return False
        