def countSwaps(a):
    i = 1 
    swaped = 0
    while(i < len(a)):
        if a[i - 1] > a[i]:
            first_place = a[i - 1]
            second_place = a[i]
            a[i - 1] = second_place
            a[i] = first_place
            swaped += 1
            i = 0
        i += 1
    print("Array is sorted in", swaped, "swaps. \n" "First Element:", a[0], "\nLast Element:", a[-1])