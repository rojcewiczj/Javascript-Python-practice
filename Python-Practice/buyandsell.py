

prices = [6,4,2,5,6,7,1,10]
buy = prices[0]
sell = prices[0]
max_profit = 0

for i in range(1, len(prices)):
    if prices[i] < buy:
        if(i < len(prices)-1):
            buy = prices[i]
            sell = prices[i+1]
            max_profit = max(max_profit, sell - buy)
    elif prices[i] > sell:
        sell = prices[i]
        max_profit = max(max_profit, sell - buy)

print(max_profit)


        
        