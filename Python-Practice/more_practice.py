
import math
import os
import random
import re
import sys
import bisect 
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

#     totals = [0] * (len(expenditure) - d)
#     checks = []
#     note = 0
#     j = 0

#     for c in range(d, len(expenditure)):
#         checks.append(expenditure[c])
    
#     def recursive(j, i):
#         totals[j] += expenditure[i]
#         print(j, i)
#         if j < len(totals) - 1:
#             j += 1
#             recursive(j, i + 1)
        
#     for i in range(0 , len(expenditure)):
#         if i < d:
#             recursive(j, i)
   
#     for t in range(0, len(totals)):
#         total = totals[t]
#         totals[t] = total // d
#         # print(totals[t],checks[t])
        
        
    i = 0

    def add(i):
        if i > 10:
            return i
        print(i)
        add(i + 1)

    add(i)
