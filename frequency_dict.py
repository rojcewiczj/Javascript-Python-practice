import math
# nums = [1,1,2,1]


# def find_single(nums):
#     my_dict = {}
    
#     for num in nums:
#         if my_dict.__contains__(num):
#             my_dict[num] += 1
#         else:
#             my_dict[num] = 1

#     for num in my_dict:
#         if my_dict[num] == 1:
#             return num
    
#     return None

# print(find_single(nums))


scores =[[1,2]
]


def every_average(scores):
    my_dict = {}
    output_list = []
    for score in scores:
        if my_dict.__contains__(score[0]):
            my_dict[score[0]].append(score[1])
        
        else:
            my_dict[score[0]] = [score[1]]

       
    for player_id in my_dict:
        my_dict[player_id].sort(reverse=True) 
        print(my_dict[player_id])
        average = 0
        total = 0
        length = 0
        for i in range(0, 5):
            if i < len(my_dict[player_id]):
                print(player_id ,my_dict[player_id][i])
                total += my_dict[player_id][i]
                length += 1
               
        
        average = math.floor(total / length)
        output_inner_list = [player_id, average]
        output_list.append(output_inner_list)
    
    return output_list


print(every_average(scores))

