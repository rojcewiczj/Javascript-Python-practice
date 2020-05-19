def minimumSwaps(arr):
    inc = 0
    count = 0

    while inc < len(arr):
        if arr[inc] > inc + 1:
            first_place = arr[inc]
            second_place = arr[first_place - 1]
            print(first_place, second_place)
            arr[inc] = second_place
            arr[first_place - 1] = first_place
            count += 1
            inc = inc - 1
    
        print(arr)
    
        print(count)
        inc += 1
        print(inc)
    return count

minimumSwaps([4,2,1,3,5,7,6])