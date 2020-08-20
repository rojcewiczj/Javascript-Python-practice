import math
import os
import random
import re
import sys
array = [2,6,1,12]
# Complete the riddle function below.
# def riddle(arr):
#     n = len(arr)
#     max_mins = [None]*n
#     stack = [] # will store (num, index)
#     for i in range(n):
#         #print('stack', stack)
#         #print('max_mins', max_mins)
#         # remember to "push back"
#         _m = i
#         while len(stack) > 0 and stack[-1][0] > arr[i]:
#             _v, _i = stack.pop(-1)
#             w = i - _i
#             for _w in range(w): # note that it's zero indexed and shifted down
#                 if max_mins[_w] is None:
#                     max_mins[_w] = _v
#                 else:
#                     max_mins[_w] = max(max_mins[_w], _v)
#             _m = _i # get the smallest index at which we could start
#         stack.append((arr[i],_m))

#     # these were the minima for all this time
#     while len(stack) > 0:
#         #print('stack', stack)
#         #print('max_mins', max_mins)
#         _v, _i = stack.pop(-1)
#         w = n - _i
#         for _w in range(w):
#             if max_mins[_w] is None:
#                 max_mins[_w] = _v
#             else:
#                 max_mins[_w] = max(max_mins[_w], _v)
#     return max_mins

# print(riddle(array))

def riddle(arr):
    
    
riddle(array)