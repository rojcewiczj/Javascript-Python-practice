

class graph:
    def __init__(self):
        self.graph = {}
    

    def insert(self, node, edges):
        self.graph[node] = edges
    
    def find_path(self, start, end, path = []):
        stack = []
        visited = []
        stack.append(start)
        while len(stack) > 0:
            current = stack.pop()
            path.append(current)
            visited.append(current)
            print(current)
            for node in self.graph[current]:
                if node == end:
                    break
            for node in self.graph[current]:
                
                    
                
                
        print(path)
            

new_graph = graph()
new_graph.insert('a', ['c'] )
new_graph.insert('b', ['c','e','f'])
new_graph.insert('c', ['a','b','d','e'])
new_graph.insert('d',['c'])
new_graph.insert('e',['c','b'])
new_graph.insert('f', ['b'])

print(new_graph.graph)
new_graph.find_path('a','f')






