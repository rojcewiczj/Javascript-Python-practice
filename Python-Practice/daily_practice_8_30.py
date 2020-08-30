array = [1,2,3,6,3,4,6,7,3,2,9,8]
ranges = {}

for i in range(len(array)):
    ranges[i] = [i,i]
    for j in range(0, i):
        if array[j] < array[i]:
            ranges[i][0] = j
            break
     
    for k in range(i , len(array)):
        if array[k] < array[i]:
            ranges[i][1] = k
            break
        

print(ranges)