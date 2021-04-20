

connections = [[1,2],[2,3],[1,4],[1,2],[3,2]]


def traverse(connections, start, end):
    queue = [[start]]
    visited = []
    while queue:
        path = queue.pop(0)
        current_node = path[-1]
        visited.append(current_node)
        if current_node == end:
            return path
        for neighbor in connections[current_node]:
            if neighbor not in visited:
                new_path = path.copy()
                new_path.append(neighbor)
                queue.append(new_path)
                


print(traverse(connections, 0, 4))