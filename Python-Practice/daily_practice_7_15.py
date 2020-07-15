def roadsAndLibraries(n, c_lib, c_road, cities):
    expense = 0
    dicti = {}
    if c_road >= c_lib:
        expense += c_lib * n
    
    else:
        for array in cities:
           
            if array[0] not in dicti:
                dicti[array[0]] = [array[1]]
            else:
                dicti[array[0]].append(array[1])
            if array[1] not in dicti:
                dicti[array[1]] = [array[0]]
            else:
                dicti[array[1]].append(array[0])
        
        stack = []
        visited = []
        path = []  
        def traverse(location,path = []):
            path = path + location
            stack.append(location)
            visited.append(location)
            
            if len(location) > 1 and len(visited) < n:
                for locations in location:
                    traverse(dicti[locations])
                   
            elif len(visited) < n:
                traverse(dicti[location[0]])
        traverse(dicti[1])
        print(path)





    
    print(dicti)