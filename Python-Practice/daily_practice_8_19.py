array = [2,6,1,12]

def riddle(arr):
    stack = []
    windows = [None] * len(arr)
    i = 0
    while i < len(arr):
        stack.append((i, arr[i]))
        

riddle(array)