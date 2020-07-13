def countTriplets(arr, r):
    first_dicti = {}
    sec_dicti = {}
    third_dicti = {}
    inc = 0
    triplets = {}
    triplet = []

    
   

    while inc < len(arr):
        first_dicti[inc] = arr[inc]
        sec_dicti[arr[inc]] = inc
        print(sec_dicti[first_dicti[inc]])
       
        inc += 1