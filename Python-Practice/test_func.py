string="whereeasttrendssouth"

def seperate(string):
    dictionary = {}
    indexes = [0]
    inc = 0
    sec_inc = 1
    new_string = []
    while(sec_inc < len(string)):
        if string[inc] == string[sec_inc]:
            indexes.append(inc)
        inc += 1
        sec_inc += 1
    
    print(indexes)

    index_inc = 0
    index_sec_inc = 1

    while index_sec_inc < len(indexes):
        dictionary[index_sec_inc] = [indexes[index_inc] + 1, indexes[index_sec_inc]]
        index_inc += 1
        index_sec_inc += 1

    print(dictionary)
    for elements in dictionary:
        new_string.append(string[dictionary[elements][0]:dictionary[elements][1]+1])
    print(new_string)
seperate(string)


