def countTriplets(arr, r):
    first_dict = {}
    sec_dict = {}

    count = 0
    
    for num in arr:
        if num not in first_dict:
            first_dict[num] = 1
        else:
            first_dict[num] += 1
    
    for i in range(1, len(arr)):
        current_num = 1
        if arr[i - 1] not in sec_dict:
            sec_dict[arr[i - 1]] = 1
        else:
            sec_dict[arr[i -1]] += 1
        if arr[i] // r in sec_dict:
            less_num = sec_dict[arr[i] // r]
        else:
            less_num = 0
        if arr[i] * r in first_dict:
            greater_num = first_dict[arr[i] * r]
        else: greater_num = 0

        count += (current_num * less_num * greater_num)
        
    return(count)
        