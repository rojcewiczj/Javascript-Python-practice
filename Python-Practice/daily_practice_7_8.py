def countTriplets(arr, r):
    first_dici = {}
    sec_dici = {}
    indexes = []
    triplets = 0

    for index, el in enumerate(arr):
        first_dici[index] = el
        if el not in sec_dici:
            sec_dici[el] = [index]
        else:
            sec_dici[el].append(index)
