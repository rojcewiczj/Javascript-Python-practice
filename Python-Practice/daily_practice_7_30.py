
def even_out(s):
    dicti = {}
    sec_dicti = {}
    array = []
    array_sec = []
   
    for letter in s:
        if letter not in dicti:
            dicti[letter]  = 1
        else:
            dicti[letter] += 1
        
    for letter in s:
        if dicti[letter] not in sec_dicti:
            sec_dicti[dicti[letter]] = 1
        else:
            sec_dicti[dicti[letter]] += 1
        
    
    for combos in sec_dicti:
        array.append(combos)
        array_sec.append(sec_dicti[combos])
        
    
    if len(array) <= 2:
        high = 0
        low  = 1
        if array[1] > array[0]:
            high = 1
            low = 0
            
        if array[high] - array[low] > 1:
            print("NO")
        elif array[low] - 1 == 0:
            print("YES")
        else:
            if array_sec[high] - 1 == array[low]:
                print("YES")
    else:
        print("NO")

    
even_out("bbccc")