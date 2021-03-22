array = [75, 105, 120, 75, 90, 135]


def find(array):
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        return array[0]
    maxSums = array.copy()
    maxSums[1] == max(maxSums[0], maxSums[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + maxSums[i])
    
    return maxSums[-1]

print(find(array))