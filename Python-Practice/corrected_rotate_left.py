def rotLeft(a, d):
    dictionary = {}
    sec_list = []
    dictionary = {}
    
    for index, num in enumerate(a):
        dictionary[index] = index - d
        sec_list.append(index)
    
    for index,num in enumerate(a):
        sec_list[dictionary[index]] = a[index]

     

    return(sec_list)
