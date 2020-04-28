S = "AABDOBECODEBANCFGHTJKLMNAJBLCASDFGAASDFHUIASDFUIHASUFHUIOASDFHAHBUDBAHDBFYHRABGDHFVBKSDFVSDBFBVBCBGYHSDCASDFFFGBCWFGTTYHBCABC"
T = "ABC"

# function for finding the shortest substring containing abc

def min_window(string, sec):
    inc = 0
    x = 0,
    y = 0
    slices = []
    abc = []
    len_dict = {}
    lengths = []
    while inc < len(string):
        if len(abc) == 0:
            if string[inc] in sec:
                x = inc
                abc.append(string[inc])
        else:
            if string[inc] in sec:
                abc.append(string[inc])
        if "A" in abc and "B" in abc and "C" in abc:
            y = inc + 1
            abc=[]

        if y != 0:
            slices.append((x,y))
            x = 0
            y = 0

        inc +=1
    
    print(slices)
    print(abc)
   
    for element in slices:
       len_dict[len(string[element[0]: element[1]])] = string[element[0]: element[1]]
       lengths.append(len(string[element[0]: element[1]]))
    
    lengths.sort()
    print(lengths)
    print(len_dict)
    print(len_dict[lengths[0]])
            




min_window(S, T)