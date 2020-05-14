def rotLeft(a, d):
    dictionary = {}
    sec_dictionary = {}

    for num in a:
        dictionary[num] = a.index(num)
    print(dictionary)
    while d > 1:
        for num in dictionary:
            if dictionary[num] == 0:
                dictionary[num] = len(a) - 1
            else: 
                dictionary[num] -= 1
        d -= 1
    
    for num in dictionary:
        a[dictionary[num]] = num

    print(a)