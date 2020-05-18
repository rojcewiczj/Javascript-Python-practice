def minimumBribes(q):
    too_chaotic = False
    sec_dicti = {}
    count = 0
    inc = len(q) - 2

    for index, num in enumerate(q):
        sec_dicti[index] = num

    while inc > - 1:
        
        if sec_dicti[inc] > sec_dicti[inc + 1]:
            first_place = sec_dicti[inc]
            second_place = sec_dicti[inc + 1]
            print(first_place, second_place)
            sec_dicti[inc + 1] = first_place
            sec_dicti[inc] = second_place
            print(sec_dicti[inc], sec_dicti[inc + 1])
            count += 1
            if inc < len(q) - 2:
                if first_place > sec_dicti[inc + 2]:
                    third_place = sec_dicti[inc + 2]
                    sec_dicti[inc + 1] = third_place
                    sec_dicti[inc + 2] = first_place
                    count += 1
                    print(sec_dicti[inc], sec_dicti[inc + 1], sec_dicti[inc + 2])
                if inc < len(q) - 3:
                    if first_place > sec_dicti[inc + 3]:
                        too_chaotic = True

        inc -= 1

    # print(sec_dicti) 
    if too_chaotic == False:
        print(count)
    else:
        print("Too chaotic")
    
minimumBribes([1,2,5,3,7,8,6,4])
       