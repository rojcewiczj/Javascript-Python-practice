def freqQuery(queries):
    dictionary = {}
    sec_dictionary = { 1 : []}
    def add(num):
        if num not in dictionary:
            dictionary[num] = 1
            sec_dictionary[dictionary[num]].append(num)
        else:
            dictionary[num] += 1
            sec_dictionary[dictionary[num]] = [num]

    def delete(num):
        if num in dictionary:
            dictionary[num] -= 1
            sec_dictionary[dictionary[num] + 1].remove(num)
    
    def find(num):
        if num in sec_dictionary:
            print(1)
        else:
            print(0)
    
    functions = {
        1 : add,
        2 : delete,
        3 : find
    }

    for query in queries:
        functions[query[0]](query[1])


