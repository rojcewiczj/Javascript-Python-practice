

def buyAndSell(prices):
    buy = prices[0]
    sell = prices[0]
    total = 0
    for i in range(1, len(prices)):
        print(buy, sell)
        if prices[i] < buy:
                buy = prices[i]
                sell = 0
        elif (prices[i] - buy) > total:
             sell = prices[i]
             total = sell - buy

    return total




print(buyAndSell([20, 99, 16, 61, 23, 16, 98, 28, 50, 40, 61, 10, 21, 70, 46, 97, 84, 67, 5, 42]))
