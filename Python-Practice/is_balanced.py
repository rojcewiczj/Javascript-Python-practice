def isBalanced(s):
    first_dici = {"{":"curl", "(":"para", "[": "brack"}
    sec_dici = {"}":"curl", ")":"para", "]": "brack"}
    first = 0
    sec = 0
    balanced = "YES"
    for index, elem in enumerate(s):
        if elem in first_dici:
            first += 1
        else:
            sec += 1
            last = s[index-1]
            if  last in first_dici and first_dici[last] != sec_dici[elem]:
                balanced = "NO"
            
    if first > sec or sec > first:
        balanced = "NO"
    
    return balanced

    # given a string of bracket types, the function will determine if the string is balanced