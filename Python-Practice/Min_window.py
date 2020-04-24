S = "ADOBECODEBANC"
T = "ABC"

def min_window(string, sec):
    indexes = []
    locations = []
    for index, element in enumerate(string):
        if element in sec:
            locations.append(index)
    




min_window(S, T)