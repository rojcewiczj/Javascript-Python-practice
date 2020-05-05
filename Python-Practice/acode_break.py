code = "asoidjfiej;akfgnrgjwalkaslkdjhfaasdfj;asdkjf;gforwarddhjfajkhfthendfijaifgturndksoejkgorightsdfupsdfasdfgg"
words= ["walk", "forward", "then", "turn", "right"]

# function for finding a message consisting of given words hidden in a jumbled string

def find_message(code, words):
    inc = 0
    dictionary = {}
    print(code)
    while inc < len(code):
        for word in words:
            if code[inc : inc + len(word)] == word :
                dictionary[code[inc : inc + len(word)]] = [inc, inc + len(word)]

        inc +=1
    
    print(dictionary)





find_message(code, words)