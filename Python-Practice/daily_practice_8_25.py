# array = [[1,-2,3],[4,2,-6,9]]
# summ = 0

# for arr in array:
#     for index, el in enumerate(arr):
#         if index == 0:
#             minimum = el
#         elif el < minimum:
#             minimum = el
#     summ += minimum
#     minimum = 0

# print(summ)
class EF_bomb:
    def __init__(self, value, location, matrix):
        self.value = value,
        self.location = location
        self.matrix = matrix
    def insert(self):
        self.matrix[self.location[0]][self.location[1]] = self.value
    
    def fall(self, fall):
        if self.matrix[self.location[0]][self.location[1] + 1] == ".":
            self.matrix[self.location[0]][self.location[1]] = "."
            self.location[1] = self.location[1] + 1
            self.insert()
            
        else:
            fall = False
            return fall
        
   

            
    
    

        
matrix = []
rows = 20
for i in range(rows):
    matrix.append(["."] * 20)

matrix[8][2] = "X"

Ef = EF_bomb("F",[0, 2], matrix)
print(Ef.location)
Ef.insert()
fall = True
while fall is True:
    Ef.fall(fall)
    


for row in matrix:
    print(row)

