def twoStrings(s1, s2):
    dictionary = {"total": 0}

    for element in s1:
        if element in dictionary:
            dictionary[element] +=1
        else:
            dictionary[element] = 1
        dictionary["total"] += 1
        
    current = dictionary["total"]

    for element in s2:
        if element in dictionary:
            dictionary["total"] -=1
        
  
    if dictionary["total"] < current:
        print("YES")
    else:
        print("NO")

twoStrings("hello", "wrd")