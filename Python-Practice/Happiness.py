# takes in an array of integers and 2 disjointed sets, you like all the integers in set A and dislike all the integers in set B

N =[1,5,3,4,6,2,1,6]
M = [[3,1],[7,2]]

def determine_happiness(array, matrix):
    happiness = 0
    if matrix[0][0] in array:
        happiness +=1
    if matrix[0][1] in array:
        happiness +=1
    if matrix[1][0] in array:
        happiness -=1
    if matrix[1][1] in array:
        happiness -=1
    print(happiness)



determine_happiness(N, M)



