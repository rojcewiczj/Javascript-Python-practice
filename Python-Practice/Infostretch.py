
brackets = "[{]}"



def isBalanced(brackets):
    stack = ["[",]
    dicti ={}
    lefts = ["[","(","{"]
    dicti["("] = ")"    
    dicti["["] = "]"
    dicti["{"] = "}"       
    
    for character in brackets:
        if character in lefts:
            stack.append(character)
        else:
            if dicti[stack.pop()] != character:
                return False
    
    if len(stack) > 0:
        return False
    
    return True
            





print(isBalanced(brackets))