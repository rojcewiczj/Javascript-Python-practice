amounts = {}

array = [ 0, 1 , 1, 3, 4]

for element in array:
    amounts[element] = 0

for element in array:
    if array.count(element) > 1:
        amounts[element] += 1

if 2 in amounts.values():
    print("yes")



