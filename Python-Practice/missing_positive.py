first_test = [1,2,0,5]
#  output: 3
second_test = [3,4,-1,1] 
# output: 2
third_test = [7,8,9,11,12] 
# output: 1
fourth_test = [0,1,2]
# output: 3

# function that outputs the lowest positive integer thats missing from array

def missing (array):
    array.sort()
    print(array)
    missing_lower = False
    lowest_positive = 0
    lowest_missing =[]
    for element in array:
        if element > 0:
            lowest_positive = element
            break
    
    if lowest_positive != 1:
        print(1)
    else:
        inc = 1
        while inc < array[-1]:
            if inc in range(1, array[-1]) and inc not in array:
                lowest_missing.append(inc)
            inc +=1
        
        if len(lowest_missing) == 0:
            print(array[-1] + 1)
        else:
            print(lowest_missing[0])


    


missing(first_test)
missing(second_test)
missing(third_test)
missing(fourth_test)