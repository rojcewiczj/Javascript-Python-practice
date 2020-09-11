array = []

for x in range(21):
    array.append([0] * 20)

print(array)

connections = {}
for x in range(len(array)):
        for y in range(len(array[x])+ 1):
            connections[f"{x},{y}"] = []
            if x + 1 < 21:
                connections[f"{x},{y}"].append([x + 1,  y])
            if x - 1 > 0:
                connections[f"{x},{y}"].append([x - 1 , y])
            if y + 1 < 21:    
                connections[f"{x},{y}"].append([x , y + 1])
            if y - 1 > 0:
                connections[f"{x},{y}"].append([x , y - 1])

# print(connections)
start = "1,1"
target = "14,18"

queue = [[start]]
visited = []
while queue:
    path = queue.pop(0)
    location = path[-1]
    if location == target:
        break
    elif location not in visited:
        for neighbor in connections[location]:
            new_path = list(path)
            new_path.append(f"{neighbor[0]},{neighbor[1]}")
            queue.append(new_path)       
        visited.append(location)
print(path)


