arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

# function that sorts arrays based on second item in nested arrays
def sort_arr():
    di = {}
    second_num = []
    for array in arr:
        second_num.append(array[1])

    second_num.sort()
  
    for array in arr:
        for element in second_num:
            if array[1] == element:
                di[element] = array
    
    sorted_array = []  
    for element in second_num:
        sorted_array.append(di[element]) 

    for array in sorted_array:
        print(array[0], array[1], array[2])
  
sort_arr()