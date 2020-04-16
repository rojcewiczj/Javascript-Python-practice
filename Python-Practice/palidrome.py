string = "tewetlhmhlmnmklkoppet"

def Longest_palidrome(string):
    palidromes =[]
    letters = {}
    palidrome = True
    inc = 0
    
    for letter in string:
        letters[letter] = []
    for letter in string:
        letters[string[inc]].append(inc)
        inc +=1
    for letter in letters:
        if len(letters[letter]) == 2:
                substring = string[letters[letter][0] : letters[letter][1] + 1]
                if len(substring) > 3:
                    if substring[1] != substring[-2]:
                        palidrome = False
                    else:
                        palidrome = True
                else:
                    palidrome = True
                if palidrome is True:
                    palidromes.append(substring)
        if len(letters[letter]) > 2:
            increment = 1
            while increment < len(letters[letter]):
                substring = string[letters[letter][increment - 1] : letters[letter][increment] + 1]
                if len(substring) > 3:
                    if substring[1] != substring[-2]:
                        palidrome = False
                    else:
                        palidrome = True
                else:
                    palidrome = True
                if palidrome is True:
                    palidromes.append(substring)
                increment += 1



                
    
       

    print(palidromes)

  
        
    
        
        

Longest_palidrome(string)