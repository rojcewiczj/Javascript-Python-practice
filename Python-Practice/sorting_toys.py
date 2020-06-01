def maximumToys(prices, k):
    print("prices:", prices)
    print(k)
    toys_bought = 0
    sorted_prices = sorted(prices)
    for toy in sorted_prices:
        if toy < k:
            toys_bought += 1
            k -= toy
    return toys_bought
