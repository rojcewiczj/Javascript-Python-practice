def NonRepeat (string):  
    dictionary = {}
    count = 0
    for element in string:
        dictionary[element] = count
    for element in string:
            dictionary[element] += 1
    for element in dictionary:
        if dictionary[element] == 1:
            print(dictionary[element])
 
       
        
   
   

    
       




NonRepeat("aabbccdde")