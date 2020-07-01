def whatFlavors(cost, money):
    dici = {}
    for index, price in enumerate(cost):
        dici[price] = index
    for index, price in enumerate(cost):
        if money - price in dici and index != dici[money - price]:
            print(index + 1, dici[money - price] + 1)
            break
