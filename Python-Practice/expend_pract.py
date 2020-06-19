#!/bin/python3

import math
import os
import random
import re
import sys
import bisect 
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    totals = [0] * (len(expenditure) - d)
    # def recursive_add(i):

        
    # def recursive_sub():

    for i in range(0 , len(expenditure)):
        if i == 0:
            totals[0]+= expenditure[i]
        if i == 1:
            totals[0] += expenditure[i]
            totals[1] += expenditure[i]
        if i == 2:
            totals[0] += expenditure[i]
            totals[1] += expenditure[i]
            totals[2] += expenditure[i]
        if i == 3:
            totals[0] += expenditure[i]
            totals[1] += expenditure[i]
            totals[2] += expenditure[i]
            totals[3] += expenditure[i]
        if i == 4:
            totals[0] += expenditure[i]
            totals[1] += expenditure[i]
            totals[2] += expenditure[i]
            totals[3] += expenditure[i]
        if i == 5:
            totals[0] += expenditure[i]
            totals[1] += expenditure[i]
            totals[2] += expenditure[i]
            totals[3] += expenditure[i]
        if i == 6:
            totals[1] += expenditure[i]
            totals[2] += expenditure[i]
            totals[3] += expenditure[i]
        if i == 7:
            totals[3] += expenditure[i]


           
            

    print(totals)
           