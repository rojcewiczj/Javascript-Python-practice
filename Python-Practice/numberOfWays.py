n = 6
denoms = [1,5]

def count(n , denoms):
    ways = [0] * (n +1)
    ways[0] =1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
                print(ways)

   


count(n , denoms)
