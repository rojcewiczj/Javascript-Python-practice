def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    color_dict = {}
    con_dict = {}
    connections = []

    for i in range(0, len(graph_from)):
        connections.append([graph_from[i], graph_to[i]])
        if graph_from[i] not in con_dict:
            con_dict[graph_from[i]] = [graph_to[i]]
        else:
            con_dict[graph_from[i]].append(graph_to[i])
        if graph_to[i] not in con_dict:
            con_dict[graph_to[i]] = [graph_from[i]]
        else:
            con_dict[graph_to[i]].append(graph_from[i])

    inc = 0
    for array in connections:
       
        if array[0] not in color_dict:
            color_dict[array[0]] = ids[inc]
            inc += 1
             
        if array[1] not in color_dict:
            color_dict[array[1]] = ids[inc]
            inc += 1
    
    for key in color_dict:
        if color_dict[key] == val:
            starting_node = key
            break
   
 
    def search(node):
        found = False
        queue = []
        queue.append([node])
        visited = [node]
        while len(queue) > 0:
            path = queue.pop(0)
            new_node = path[-1]
            if new_node not in visited:
                visited.append(new_node)
                if color_dict[new_node] == val:
                    found = True
                    break
            for nodes in con_dict[new_node]:
                if nodes not in visited:
                    new_path = list(path)
                    new_path.append(nodes)
                    queue.append(new_path)
        path.pop(-1)
        if found is True:
            return len(path)
        else:
            return -1

    return search(starting_node)
    