array = [7,5,9,2,9]

def jump(arr):
    dictionary = {}
    for index, num in enumerate(array):
        dictionary[num] = index
    print(dictionary)
    sorted_arr = []
    for num in array:
        sorted_arr.append(num)

    sorted_arr.sort()
    print(sorted_arr)
    j = dictionary[sorted_arr[0]]
    k = dictionary[sorted_arr[0]]
    print(j,k)

    while  k + 1 < len(arr):
        if arr[j - 1] > arr[j] and j > 0:
            j = j - 1
        if arr[k + 1] > arr[k]:
            k = k + 1
    max_distance = k - j
    print(j, k)
    print(max_distance)
    
 




jump(array)