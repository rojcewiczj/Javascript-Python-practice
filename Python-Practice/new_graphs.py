
array = [[1,2],[1,3],[3,2],[3,4],[4,6],[6,8]]

dicti = {}

for ar in array:
    if ar[0] not in dicti:
        dicti[ar[0]] = [ar[1]]
    else:
        dicti[ar[0]].append(ar[1])
    if ar[1] not in dicti:
        dicti[ar[1]] = [ar[0]]
    else:
        dicti[ar[1]].append(ar[0])

print(dicti)

queue = [[1]]
visited = []
while len(queue) > 0:
    path = queue.pop(0)
    current = path[-1]
    if current not in visited:
        for neighbor in dicti[current]:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
        visited.append(current)
path.pop(-1)


print(path)