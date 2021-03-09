class BST:
    def __init__(self, root):
        self.root = root

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    

   
#      5
#   10    25
# None None    12     3
rootNode = Node(5)
rootNode.left = Node(10)
rootNode.left.left = Node(67)
twentyFiveNode = Node(25)
rootNode.right = twentyFiveNode
twelveNode = Node(12)
twentyFiveNode.left = twelveNode
threeNode = Node(3)
twentyFiveNode.right = threeNode
sixNode = Node(6)
sevenNode = Node(7)
# twelveNode.left = Node(30)
# twelveNode.right = Node(40)
BinaryTree = BST(rootNode)


def traverse(root):
    queue = [root]
    return_list = []
    levels = [1]
    dicti = {}
    i = 0
    while(queue):
        node = queue.pop(0)
        if(node == None):
            return_list.append(None)
            continue
        return_list.append(node.value)
        if(node.left):
            queue.append(node.left)
            levels.append(levels[i] + 1)
        else:
            levels.append(levels[i] + 1)
            queue.append(None)
        if(node.right):
            queue.append(node.right)
            levels.append(levels[i] + 1)
        else:
            levels.append(levels[i] + 1)
            queue.append(None)
        i += 1
    
    for i in range(0, len(levels)):
        if levels[i] not in dicti:
            dicti[levels[i]] = [return_list[i]]
        else:
            dicti[levels[i]].append(return_list[i])
        
   
    
    print(levels)
    print(dicti)
    return dicti

def is_balanced(dicti):
    maximum_level = 999
    for key in dicti:
        if None in dicti[key]:
            maximum_level = min(maximum_level, key) 
        if key > maximum_level:
            for el in dicti[key]:
                if el is not None:
                    return False
    return True
            
print(is_balanced(traverse(BinaryTree.root)))
       
            



    







    


        