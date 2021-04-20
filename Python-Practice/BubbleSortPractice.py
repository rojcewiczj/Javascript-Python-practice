numbers = [47,24,13,12,10,96,35]

def BubbleSort(array):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
                swap = True
    return array

print(BubbleSort(numbers))
   