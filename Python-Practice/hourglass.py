def hourglassSum(arr):
    first_line=[]
    second_line=[]
    third_line=[]
    first_line_inc = 0
    second_line_inc = 1
    third_line_inc = 2
    first_and_third_inc = 0
    sec_inc = 1

    while third_line_inc < 6:
        while first_and_third_inc + 3 < 7:
            first_line.append([arr[first_line_inc][first_and_third_inc],arr[first_line_inc][first_and_third_inc + 1],arr[first_line_inc][first_and_third_inc + 2]])
            
            if sec_inc < 5:
                second_line.append(arr[second_line_inc][sec_inc])
                sec_inc += 1

            third_line.append([arr[third_line_inc][first_and_third_inc],arr[third_line_inc][first_and_third_inc + 1],arr[third_line_inc][first_and_third_inc + 2]])

            first_and_third_inc += 1

        first_line_inc += 1
        second_line_inc += 1
        third_line_inc += 1
        first_and_third_inc = 0
        sec_inc = 1
    
    inc_for_add = 0
    totals = []
    while inc_for_add < 16:
        totals.append(first_line[inc_for_add][0] + first_line[inc_for_add][1] + first_line[inc_for_add][2] + second_line[inc_for_add] + third_line[inc_for_add][0] + third_line[inc_for_add][1] + third_line[inc_for_add][2])
        
        inc_for_add += 1


    totals.sort()
    print(totals[-1])

    
hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])