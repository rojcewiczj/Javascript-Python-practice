# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         digits = []
        
#         is_add = True
        
#         for character in num:
#             digits.append(int(character))
            
#         print(digits)
        
#         inc = 1
        
#         while inc < len(digits) - 1:
#             if digits[inc-1] + digits[inc] == digits[inc+1]:
#                 print(digits[inc-1],digits[inc], digits[inc+1])
#                 inc+= 1
#             else:
#                 is_add = False
#                 break
                
#         return is_add
import ast



class Room:
    def __init__(self):
        self.n_to = "room"



room = Room()

print(room.n_to)

