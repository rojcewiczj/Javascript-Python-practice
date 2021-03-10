matrix = [[1,3,5,2],
          [3,7,6,9],
          [2,8,4,3],
          [7,9,3,0]]

def traverse(matrix):
    diagonals=[matrix[0][0]]
    x_count = 0
    while(x_count < len(matrix)):
        y = 0
        diag = []
        x = x_count
        while(x >= 0):
            diag.append(matrix[x][y])
            x -= 1
            y += 1
        diag.sort()
        diagonals.append(diag)
        x_count += 1

    x_count = len(matrix) - 1
    while(x_count >= 1):
        y = len(matrix[0]) -1
        diag = []
        x = x_count
        while(x <= len(matrix) -1):
            print(matrix[x][y])
            diag.append(matrix[x][y])
            x += 1
            y -= 1
        diag.sort()
        diagonals.append(diag)
        x_count -= 1

    

   

    print(diagonals)
    print(matrix)
traverse(matrix)

nums = [10,1,2,3,4,5]

removed_once = False

for i in range(1, len(nums)):
    if nums[i-1] > nums[i] and removed_once is False:
        removed_once = True
    else:
        print(False)
    
