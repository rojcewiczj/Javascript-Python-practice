array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

lowest = 0
total = 0

for arr in array:
    for el in arr:
        if el == arr[0]:
            lowest = el
        if el < lowest:
            lowest = el
            
    print(lowest)
    total += lowest
    lowest = 0

print(total)