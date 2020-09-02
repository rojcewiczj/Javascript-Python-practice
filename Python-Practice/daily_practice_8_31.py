# array = [1,2,3,6,3,4,6,7,3,2,9,8]
# ans = 0
# i = 0
# stack = []
# while i < len(array):
#     if len(stack) == 0 or array[stack[-1]] <= array[i]:
#         stack.append(i)
#         i += 1
#     else:
#         height = array[stack.pop(-1)]
#         if len(stack) > 0:
#             size = height * (i - stack[-1] - 1)
#         else:
#             size = height * i
        
#         if size > ans:
#             ans = size

# while len(stack) > 0:
#     height = array[stack.pop(-1)]
#     if len(stack) > 0:
#         size = height * (len(array)- stack[-1] - 1)
#     else:
#         size = height * len(array)
#     if size > ans:
#         ans = size
    
#     print(ans)

array = ['Waltz', "Waltz",'Tango','Tango','Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

set1 = set(array)

print(set1)

dictionary = {}
sec_dict = {}

for word in array:
    if word not in dictionary:
        dictionary[word] = 1
        if dictionary[word] not in sec_dict:
            sec_dict[dictionary[word]] = [word]
        else:
            sec_dict[dictionary[word]].append(word)
    else:
        sec_dict[dictionary[word]].remove(word)
        if dictionary[word] +1 not in sec_dict:
            sec_dict[dictionary[word]+1]=[word]
        else:
            sec_dict[dictionary[word]+1].append(word)

        dictionary[word] += 1

print(dictionary)
print(sec_dict)
print(sec_dict[2])


    