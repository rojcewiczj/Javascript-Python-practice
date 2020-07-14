class province:
    def __init__(self, number_of_cities, cities, library_cost, road_cost):
        self.number_of_cites = number_of_cities
        self.cities = cities
        self.library_cost = library_cost
        self.road_cost = road_cost
        self.expense = 0

class city:
    def __inti__(self, name, roads):
        self.name = name
        self.roads = roads
        self.library = None
class road:
    def __init__(self, condition, connection):
        self.condition = condition
        self.connection = connection

class library:
    def __init__ (self, name, location):
        self.name = name
        self.location = location

class repair_man:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def repair_road(self, city, province):
        province.expense += province.road_cost
        city.roads.condition = "fixed"
    
    def build_library(self, city, province, library):
        province.expense += province.library_cost
        city.library = library





# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    print("number of cities: ", n)
    print("cost of library: ", c_lib)
    print("cost of repairing a road: ", c_road)
    print("city connections: ", cities)
    dicti = {}
    sec_dicti = {}
    for connection in cities:
        if connection[0] not in dicti:
            dicti[connection[0]] = [connection[1]]
            sec_dicti[connection[0]] = ["?"]
        else:
            dicti[connection[0]].append(connection[1])
       
        if connection[1] not in dicti:
            dicti[connection[1]] = [connection[0]]
          
        else:
            dicti[connection[1]].append(connection[0])
          
    visited = [1]
    stack = []

    
               
    print(visited)
    print(dicti)