code = "asoidjfiej;akfgnrgjlookaslkdjhfasdfupsdfasdfgg"
words= ["look", "up"]

# function for finding a message consisting of given words hidden in a jumbled string

def find_message(code, words):
    inc = 0
    message = []
    print(code)
    while inc < len(code):
        for word in words:
            if code[inc : inc + len(word)] == word :
                message.append(code[inc : inc + len(word)])

        inc +=1
    
    print(message)





find_message(code, words)