def substrCount(n, s):
    to_compare = s[0]
   
    letters = []
    dictionary = {}
   
    for index, letter in enumerate(s):
        letters.append((letter, index))
        
    for pair in letters:
        for sec_pair in letters:
            if sec_pair[0] == pair[0] and sec_pair[1] != pair[1]:
                if sec_pair[1] - pair[1] == 1:
                    if s[pair[1]: sec_pair[1] + 1] not in dictionary:
                        dictionary[s[pair[1]: sec_pair[1] + 1]] = 1
                    else:
                        dictionary[s[pair[1]: sec_pair[1] + 1]] += 1
                if sec_pair[1] - pair[1] == 2:
                    if s[pair[1]: sec_pair[1] + 1] not in dictionary:
                        dictionary[s[pair[1]: sec_pair[1] + 1]] = 1
                    else:
                        dictionary[s[pair[1]: sec_pair[1] + 1]] += 1
                if sec_pair[1] - pair[1] > 2:
                    for i in range(pair[1], sec_pair[1]):
                        if s[i] != pair[0]:
                            works = True
                            if pair[0] == s[sec_pair[1] - ((sec_pair[1] - pair[1]) // 2)]:
                                if s[pair[1]: sec_pair[1] + 1] not in dictionary:
                                    dictionary[s[pair[1]: sec_pair[1] + 1]] = 1
                                else:
                                    dictionary[s[pair[1]: sec_pair[1] + 1]] += 1
                                
                        else:
                            pass
    print(letters)                
    print(dictionary)
