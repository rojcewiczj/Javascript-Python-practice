def checkMagazine(magazine, note):
    can_use = True
    dictionary = {}
  
    for word in magazine:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    for word in note:
        if word in dictionary:
            dictionary[word] -= 1
            if dictionary[word] < 0:
                can_use = False
        else:
            can_use = False

     
    if can_use == True:
        print("Yes")
    else:
        print("No")

checkMagazine(["hello", "how", "are", "you"],["Hey", "how", "are", "you"])