def minimumBribes(q):
    too_chaotic = False
    count = 0
    inc = len(q) - 2
    while inc > - 1:
        if  q[inc] > q[inc + 1]:
            first_place = q[inc]
            second_place = q[inc + 1]
            print(first_place, second_place)
            q[inc + 1] = first_place
            q[inc] = second_place
            print(q[inc], q[inc + 1])
            count += 1
            if inc < len(q) - 2:
                if first_place > q[inc + 2]:
                    third_place = q[inc + 2]
                    q[inc + 1] = third_place
                    q[inc + 2] = first_place
                    count += 1
                    print(q[inc], q[inc + 1], q[inc + 2])
                if inc < len(q) - 3:
                    if first_place > q[inc + 3]:
                        too_chaotic = True

        inc -= 1

    # print(sec_dicti) 
    if too_chaotic == False:
        print(count)
    else:
        print("Too chaotic")
    
minimumBribes([1,2,5,3,7,8,6,4])
       