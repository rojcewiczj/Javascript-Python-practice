

def rotLeft(a, d):
    sec_list = []
    dictionary={}
    inc = -1
    for num in range(0, len(a)):
        inc +=1
        sec_list.append(inc)
        dictionary[num] = sec_list.index(sec_list[inc])
    
    while d > 0:
        for num in dictionary:
            if dictionary[num] == 0:
                dictionary[num] = len(a) - 1
            else:
                dictionary[num] -= 1
            sec_list[dictionary[num]] = a[num]    
        d -=1
    print(dictionary)
      
    return sec_list

    print(a)