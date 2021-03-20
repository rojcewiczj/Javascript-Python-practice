memory = [0,1,0,0,1,1,1,1,0,0,0,1]
queries = [[0,2],[1,1],[0,3],[1,11]]





def readQueries(queries, memory):
    results = []
    for query in queries:
        if query[0] == 0:
            returned = allocate(query, memory)
            if len(returned) > 1:
                memory = returned[0]
                results.append(returned[1])
            else:
                results.append(returned[0])
        else:
            if query[0] == 1:
                memory[query[1]] = 0

    print(memory, results)
            
            


def allocate(query, memory):
    start = 0
    end = query[1] 
    to_return = []
    while end <= len(memory):
        valid = True
        for i in range(start, end):
            if memory[i] == 1:
                valid = False
                break
        if valid:
            for i in range(start,end):
                memory[i] = 1
            break
        start += 1
        end += 1
    
    if valid:
        to_return.append(memory)
        to_return.append(start)
        return to_return
    else:
        to_return.append(-1)
        return to_return
        
             
            
                
readQueries(queries, memory)
    
