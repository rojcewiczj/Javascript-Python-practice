string="whereeasttrendssouthhouse"

def seperate(string):
    print(string[0:5])
    dictionary = {1:[0,5]}
    indexes = [0]
    inc = 0
    sec_inc = 1
    while sec_inc < len(string):
        if string[inc] == string[sec_inc]:
            indexes.append(sec_inc)
        inc +=1
        sec_inc +=1
    indexes.append(len(string))
    
    index_inc = 0
    index_inc_two = 1

    while index_inc_two < len(indexes):
        dictionary[index_inc_two] = [indexes[index_inc], indexes[index_inc_two]]
        index_inc +=1
        index_inc_two +=1
    
    print(dictionary)
    print(indexes)
    
    new_words = []
    for element in dictionary:
        new_words.append(string[dictionary[element][0]:dictionary[element][1]])

    print(new_words)


seperate(string)