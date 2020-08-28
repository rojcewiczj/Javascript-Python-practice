array = [1,3,4,5,2,4,5,6,4]


first = 0
queue = [first]
towers = []
i = 1
while i < len(array):
    if len(queue) > 0:
        last = queue[0]
    print(queue)
    if i - last == 2:
        lesser = queue.pop(0)
        print(lesser)
        greater = array[i]
        print(greater)
        length = i - last
        size = length * greater
        towers.append(size)
    else:
        queue.append(i)
    i += 1

print(towers)
