



def balancedOrNot():
    stack = []
    string = "[{[]"
    lefts = "({["
    dictionary = {
        ")":'(',
        "]":'[',
        '}': '{'
    }
    for para in string:               
        if para in lefts:
            stack.append(para)
        else:
            if len(stack) == 0:
                return False
            else:
                if(stack[-1] == dictionary[para]):
                    stack.pop(-1)
                else:
                    return False

    if len(stack) == 0:
        return True
    else:
        return False

print(balancedOrNot())
            


