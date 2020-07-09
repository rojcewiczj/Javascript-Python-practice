# def countTriplets(arr, r):
#     first_dici = {}
#     sec_dici = {}
#     indexes = []
#     triplets = 0

#     for index, el in enumerate(arr):
#         first_dici[index] = el
#         if el not in sec_dici:
#             sec_dici[el] = [index]
#         else:
#             sec_dici[el].append(index)


# arrays = [[1,2],[3,4]]

# lowest = 0
# total = 0

# for array in arrays:
#     lowest = min(array)
#     total += lowest

# print(total)
        

string = "asdkkkkfj;aksdjf"
to_ignore = [";"]
total = 0
dicti  = {}
freq_dicti = {}
for letter in string:
    if letter not in to_ignore:
        total += 1
        if letter not in dicti:
            dicti[letter] = 1
        else:
            dicti[letter] += 1

for letter in dicti:
    freq_dicti[letter] = (dicti[letter] / total) * 100

print("total: ", total, "amount: ", dicti, "freq :", freq_dicti)



