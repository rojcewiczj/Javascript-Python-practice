n = 7
denoms = [1,5, 10]

def find(n, denoms):
    numOfCoins = [float('inf')] * (n + 1)
    numOfCoins[0] = 0
    toCompare = 0

    for denom in denoms:
        for amount in range(0, len(numOfCoins)):
            if denom <= amount:
                if numOfCoins[amount - denom] == float('inf'):
                    toCompare = numOfCoins[amount - denom]
                else:
                    toCompare = numOfCoins[amount - denom] +1
                
                numOfCoins[amount] = min(numOfCoins[amount], toCompare)
        print(numOfCoins)
    if numOfCoins[n] != float('inf'):
       return numOfCoins[n]
    else:
       return -1




print(find(n, denoms))

