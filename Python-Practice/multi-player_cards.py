

def player_cards(num_of_players, deck):
    rounds = [0] * (len(deck) // num_of_players)
    nums = [0] * num_of_players
    check = len(deck) - num_of_players - 1
    
    i = len(rounds)
    l = 0
    k = 0
    while i > 0:
        max = 0
        for j in reversed(range(check + 1, check + num_of_players + 1)):
            nums[k] = deck[j]
            if nums[k] > max:
                highest = k + 1
                max = nums[k]
           
            k += 1
        
        rounds[l] = highest
        l += 1
        k = 0
        max = 0
        check = check - num_of_players 
        print(nums, highest, rounds, l)
        nums = [0] * num_of_players
        i -= 1
    


player_cards(3,[1,2,5,3,1,7,8,4,6,3,9,5])