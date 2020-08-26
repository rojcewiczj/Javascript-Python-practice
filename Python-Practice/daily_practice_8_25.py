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

class Ef:
    def __init__(self, value, mappy):
        self.value = value
        self.map = mappy
        self.location = []
        self.neighbors = []
    def get_neighbors(self):
        self.neighbors = []
        self.neighbors.append(self.map[self.location[0] + 1][self.location[1]])
        self.neighbors.append(self.map[self.location[0] -1 ][self.location[1]])
        self.neighbors.append(self.map[self.location[0]][self.location[1] + 1])
        self.neighbors.append(self.map[self.location[0]][self.location[1] - 1])
    def move(self):
        directions = {
            "w": self.neighbors[1],
            "s": self.neighbors[0],
            "d": self.neighbors[2],
            "a": self.neighbors[3]
        }
        dir = input("enter a direction :")
        print(dir)
        if dir not in directions:
             dir = input("enter a direction :")
             print(dir)
        if directions[dir] != "X":
            if dir  == "w":
                self.location[0] -= 1 
                self.map[self.location[0] + 1][self.location[1]] = "."
            if dir == "s":
                self.location[0] += 1
                self.map[self.location[0] - 1][self.location[1]] = "."
            if dir == "d":
                self.location[1] += 1
                self.map[self.location[0]][self.location[1] - 1] = "."
            if dir == "a":   
                self.location[1] -= 1
                self.map[self.location[0]][self.location[1] + 1] = "."
            self.map[self.location[0]][self.location[1]] = "F"
            self.get_neighbors()
           
         
            for row in self.map:
                print(row)
            
        


    
        
        

class matrix:
    def __init__(self):
        self.arrays = []
    def generate(self):
        for i in range(21):
            if i == 0 or i == 20:
                self.arrays.append(["X"] * 20)
            else:
                self.arrays.append(["."] * 20)
                self.arrays[i][0] = "X"
                self.arrays[i][-1] = "X"
    def print_map(self):
        for row in self.arrays:
            print(row)
    def insert(self, x,y,value):
        self.arrays[x][y] = value.value
        value.location = [x, y]
    
    


                



    

running = True
map = matrix()
map.generate()
elem = Ef("F", map.arrays)
ex = Ef("X", map.arrays)
map.insert(1,2, elem)
map.insert(3,3, ex)
elem.get_neighbors()

map.print_map()

while running:
    elem.move()