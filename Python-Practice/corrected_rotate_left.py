

def rotLeft(a, d):
    dictionary = {}
    sec_list = []
    dictionary = {}
    
    for index, num in enumerate(a):
        dictionary[index] = index - d
        sec_list.append(index)
    
    for index,num in enumerate(a):
        sec_list[dictionary[index]] = a[index]

     

    print(sec_list)

rotLeft([1,2,3,4,5,6], )