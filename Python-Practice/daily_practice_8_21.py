# string = "thyoiyouthlklklthth"
# count = 0
# i = 0
# j = 1

# def find_th(count, string, i, j):
#         if j+ 1 <= len(string):
#             if string[i:j + 1] == "th":
#                 count += 1
#             find_th(count,string,i +1, j + 1)
#         else:
#             print(count)

# find_th(count, string, i, j)

eggs = 30
floors = [i for i in range(0, 100000)]
print(floors)
target = 42

def find_min(floors, target, eggs):
    low = 0
    mid = 0
    high = len(floors) - 1

    while mid != target:
        mid = (low + high) // 2
        eggs -= 1
        if floors[mid] < target:
            low = mid + 1
        
        elif floors[mid] > target:
            high = mid - 1
           
           
        else:
            return eggs
    

    
        
print(find_min(floors, target, eggs))
        

