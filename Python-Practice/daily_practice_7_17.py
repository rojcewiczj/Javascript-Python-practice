def countTriplets(arr, r):
    first_dict = {}
    sec_dict = {}
    count = 0
    for i in range(0, len(arr)):
        if arr[i] not in first_dict:
            first_dict[arr[i]] = 1
        else:
            first_dict[arr[i]] += 1
        if arr[i] == arr[0]:
            pass
        else:
            if arr[i] != arr[0]:
                past_elem = arr[i -1]
                if past_elem not in sec_dict:
                    sec_dict[past_elem] = 1
                else:
                    sec_dict[past_elem] += 1
        
            current_elem = arr[i]
            print(sec_dict[current_elem // r], first_dict[current_elem * r])
            first_dict[current_elem] -= 1

            if (current_elem // r) in sec_dict and (current_elem * r) in first_dict:
                print("yes")
                count += sec_dict[current_elem // r] * first_dict[current_elem * r]
        