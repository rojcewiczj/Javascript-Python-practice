text = "laalaxcmbdtsumbdav"

def find(text):
    output = 0
    dicti = {}
    word = "sum"
    for letter in word:
        dicti[letter] = 0
    for letter in text:
        if letter in word:
            dicti[letter] += 1
    
    check_word = ""
    done = False
    while done == False:
        for letter in word:
            if dicti[letter] != 0:
                check_word += letter
                dicti[letter] -= 1
                print(dicti)
                print(check_word)
            else:
                done = True
                break
        if check_word == word:
            output += 1
        check_word = ""

    
    return output

   




print(find(text))