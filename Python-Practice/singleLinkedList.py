
def compress(string):
    dictionary = {}
    for element in string:
        dictionary[element] = 0

    for element in string:
        dictionary[element] +=1
        
    for element in dictionary:
        print ((dictionary[element], element))
compress("1222311")