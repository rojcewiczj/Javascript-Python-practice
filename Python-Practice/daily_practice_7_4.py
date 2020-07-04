array = []
dici = {}

for num in range(0, 100):
    array.append(num)

for num in array:
    if num % 2 == 0:
        dici[num] = array.index(num)

print(dici)

    