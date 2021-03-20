graph = [[1,2],[3],[3],[4],[]]


all_path = []

def traverse(starting_node, ending_node):
    all_path = []
    stack = [[starting_node]]
    while(len(stack) > 0):
        current_path = stack.pop(-1)
        current_node = current_path[-1]
        if current_node == ending_node:
            all_path.append(current_path)
        else:
            for neighbor in graph[current_node]:
                new_path = current_path.copy()
                new_path.append(neighbor)
                stack.append(new_path)
                
    return all_path
print(traverse(0, 4))



    