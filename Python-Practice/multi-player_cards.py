

def player_cards(num_of_players, deck):
    dicti = {}
    i = num_of_players
    for i in range(1, num_of_players + 1):
        dicti[i] = []
    print(dicti)
    i = 1
    j = len(deck) - 1
    while j > -1:
        print(i)
        dicti[i].append(deck[j])
        if i == num_of_players:
            i = 1
        else:
            i += 1
        
        j -= 1

    print(dicti)
    rounds = [0] * (len(deck) // num_of_players)
    for i in range(0,len(rounds)):
        for key in dicti:
            if dicti[key][i + 1] > rounds[i]:
                
    print(rounds)


player_cards(3,[1,2,5,3,1,7,8,4,6,3,9,5])