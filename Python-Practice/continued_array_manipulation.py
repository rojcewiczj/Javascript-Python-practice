def arrayManipulation(n, queries):
    highest = 0
    inc = 0
    array = []
    for num in range(1, n + 1):
        array.append(0)
        for query in queries:
            if num in range(query[0], query[1] + 1):
                array[num - 1] += query[2]
                if array[num - 1] > highest:
                    highest = array[num -1]
    return(highest)
