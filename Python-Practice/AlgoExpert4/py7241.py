def findLetter(word, letter):
    found = []
    for i in range(len(word)):
        if word[i] == letter:
            found.append(str(i))

    found = "".join(found)
    return found
    



print(findLetter("asdfasdfadfadfg", "a"))