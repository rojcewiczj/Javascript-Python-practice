def countTriplets(arr, r):
    first_dicti = {}
    
    def in_list(el, arr):
        if el * r in arr and el * r *r in arr:
            return True

    def forms_triplet(el,index):
        if first_dicti[el] is not None:
            first_dicti[el][0].append(index)
        
    for index, el in enumerate(arr):
        if in_list(el, arr):