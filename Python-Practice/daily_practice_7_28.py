# def freqQuery(queries):

#     first_dict = {}
#     sec_dict = {}

#     def add(elem):
#         if elem not in first_dict:
#             first_dict[elem] = 1
#         else:
#             first_dict[elem] += 1
    
#         if first_dict[elem] not in sec_dict:
#             sec_dict[first_dict[elem]] = [elem]
#         else:
#             sec_dict[first_dict[elem]].append(elem)

#     def subtract(elem):
#         if elem not in first_dict:
#             print(0)
#         else:
#             for index, freq in enumerate(sec_dict[first_dict[elem]-1]):
#                 if freq == elem:
#                     sec_dict[first_dict[elem]].pop(index)
            
#             first_dict[elem] -= 1

#     def check(freq):
#         if freq in sec_dict:
#             if len(sec_dict[freq]) > 0:
#                 print(1)
#             else:
#                 print(0)
#         else:
#             print(0)


#     functions = {
#         1 : add,
#         2 : subtract,
#         3 : check
#     }

#     for query in queries:
#         functions[query[0]](query[1])

#     print(first_dict)
#     print(sec_dict)

# freqQuery([[1,1],[1,1],[2,1],[1,1],[3,1]])

# array = [2,7,1,15] 
# target = 9
# x = 0
# y = 0

# for index, num in enumerate(array):
#     if target - num in array:
#         x = index
#         to_find = target - num
#     if num == to_find:
#         y = index

# print([y,x])

array = ["eat", "tea", "hope", "opeh"]

dicti = {}

for word in array:
    sorted_string = "".join(sorted(word))
    if sorted_string not in dicti:
        dicti[sorted_string] = [word]
    else:
        dicti[sorted_string].append(word)


    




       