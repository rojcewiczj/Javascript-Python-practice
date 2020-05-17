def minimumBribes(q):
    too_chaotic = False
    inc = len(q) - 1
    dicti = {}
    sec_dicti = {}
    count = 0
    dicti[q[inc]] = inc
    sec_dicti[inc] = q[inc]
    while inc > -1:
        inc -=1
        dicti[q[inc]] = inc
        sec_dicti[inc] = q[inc]
        print(dicti)
        print(sec_dicti)
       
        
        
        
    
    print(dicti)
            