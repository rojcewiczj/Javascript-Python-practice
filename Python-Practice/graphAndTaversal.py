class Graph:
    def __init__(self, adjList):
        self.adjList = adjList
    
    def Tarverse(self, start, end):
        queue = [[start]]
        visited = []
        current = start
       
        while len(queue) and current != end:
            cur_path = queue.pop(0)
            current = cur_path[-1]
            visited.append(current)
            for neighbor in self.adjList[current]:
                if neighbor not in visited:
                    new_path = cur_path.copy()
                    new_path.append(neighbor)
                    queue.append(new_path)
                    print(new_path)
                    break





TestGraph = Graph([[0,1],[1,2],[2,4],[2,4],[4,3]])
TestGraph.Tarverse(0, 4)