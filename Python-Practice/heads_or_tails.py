array = [1,0,1,0,1,1,1]
def flip(arr):
    correct_form =[]
    inc = 0
    flips = 0
    while inc < len(arr):
        if arr[0] == 0 and len(correct_form) == 0:
            correct_form.append(0)

        elif arr[0] == 1 and len(correct_form) == 0:
            correct_form.append(1)
        else:
            if arr[0] == 0:
                if inc % 2 == 1:
                    correct_form.append(1)
                else:
                    correct_form.append(0)
            elif arr[0] == 1:
                if inc % 2 == 1:
                    correct_form.append(0)
                else:
                    correct_form.append(1)
        if arr[inc] != correct_form[inc]:
            flips += 1
        inc += 1        

    print(flips)   
    print(correct_form)

        
        


        


flip(array)