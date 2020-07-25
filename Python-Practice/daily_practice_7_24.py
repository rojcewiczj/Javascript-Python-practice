edges = [[1,2],[2,3],[3,4],[1,5]]

con_dict = {}

for array in edges:
    if array[0] not in con_dict:
        con_dict[array[0]] = [array[1]] 
    else:
        con_dict[array[0]].append(array[1])
    if array[1] not in con_dict:
        con_dict[array[1]] = [array[0]]
    else:
        con_dict[array[1]].append(array[0])

print(con_dict)
distance = {}
starting_node = 1
def search():
    queue = [[starting_node]]
    visited = [starting_node]
    while len(queue) > 0:
        path = queue.pop(0)
        node = path[-1]
        print(path, node)
        for connection in con_dict[node]:
            if connection not in visited:
                distance[connection] = (len(path)) 
                new_path = list(path)
                new_path.append(connection)
                queue.append(new_path)
                visited.append(connection)
            
    return path

path = search()

print(distance)








    
    