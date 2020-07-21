def roadsAndLibraries(n, c_lib, c_road, cities):
    dicti = {}
    total_cost = 0
  

    if c_lib < c_road:
        total_cost += c_lib * n
    else:

        for connection in cities:
      
            if connection[0] < connection[1]:
                if connection[0] not in dicti:
                    dicti[connection[0]] = [connection[1]]
                  
                else:
                    dicti[connection[0]].append(connection[1])
            if connection[1] < connection[0]:
                if connection[1] not in dicti:
                    connection[1] = [connection[0]]
               
                else:
                    dicti[connection[1]].append(connection[0])
                  

        for entery in dicti:
            total_cost += c_lib
            total_cost += c_road * (len(dicti[entery]))
            print(total_cost)

        print(dicti)
        print(total_cost)
        