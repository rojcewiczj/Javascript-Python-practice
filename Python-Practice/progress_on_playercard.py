

def player_cards(num_of_players, deck):
    rounds = len(deck) // num_of_players
    wins = [0] * num_of_players
    nums = [0] * num_of_players
    check = len(deck) - num_of_players - 1
    
    i = rounds
    l = 0
    k = 0
    while i > 0:
        max = 0
        for j in reversed(range(check + 1, check + num_of_players + 1)):
            nums[k] = deck[j]
            if nums[k] > max:
                highest = k 
                max = nums[k]
           
            k += 1
        
        wins[highest] += 1
        l += 1
        k = 0
        max = 0
        check = check - num_of_players 
        
        print(nums, wins)
        nums = [0] * num_of_players
        i -= 1

    
    winner = [0, wins[0]]
    for index,elem in enumerate(wins):
        if index > 0:
            if elem > winner[1]:
                winner = [index, elem]
            
    print(f"Player {winner[0] + 1} wins with {winner[1]} wins")


