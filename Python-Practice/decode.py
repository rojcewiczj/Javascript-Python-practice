import math
import os
import random
import re
import sys






matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']


 
def decode(matrix):
    column_one = []
    column_two = []
    column_three = []
    decoded_message = []

    for string in matrix:

       column_one.append(string[0])
       column_two.append(string[1])
       column_three.append(string[2])

    column_two.extend(column_three)
    column_one.extend(column_two)
   
    for index, element in enumerate(column_one):
        di_true = {True : column_one[index], False: ' '}
        decoded_message.append(di_true[element.isalnum()])

    print(decoded_message)
decode(matrix)