starting_node = 1

edges = [[1,2],[2,3],[3,4],[1,5]]

dicti = {}

for array in edges:
    if array[0] not in dicti:
        dicti[array[0]] = [array[1]]
    else:
        dicti[array[0]].append(array[1])
    if array[1] not in dicti:
           dicti[array[1]] = [array[0]]
    else:
        dicti[array[1]].append(array[0])

print(dicti)
dead_ends = []
queue = []
queue.append([starting_node])
visited = []

while len(queue) > 0:
    path = queue.pop(0)
    node = path[-1]
    visited.append(node)  
    if len(dicti[node]) == 1:
        if dicti[node][0] == starting_node:
            dead_ends.append(node)
    for neighbor in dicti[node]:
        if neighbor not in visited:
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
print(path)
final_path = []
step = 6
for node in path:
    final_path.append(step)
    step += 6
for node in dead_ends:
    final_path.append(-1)

print(final_path)
    




    


    