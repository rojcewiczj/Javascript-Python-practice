
strs = ["ear","apt", "pat","tap", "are", "arm"]

def anagramSort(strs):
    dicti = {}
    output = []
    sec_dicti = {}
    if len(strs) <= 1:
        return [[""]]
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in dicti:
            dicti[sorted_word] = [word]
        else:
            dicti[sorted_word].append(word)
    lengths = []
    for key in dicti:
        sec_dicti[len(dicti[key])] = dicti[key]
        lengths.append(len(dicti[key]))
    
    lengths.sort(reverse=True)
    
    for length in lengths:
        output.append(sec_dicti[length])
    
    return output
print(anagramSort(strs))