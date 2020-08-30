array = [1,3,4,5,2,4,5,6,4]


stack = []
towers = []
i = 0
while i < len(array):
    if len(stack) == 0:
        stack.append(i)
    else:
        while len(stack) > 0:
            check = stack[-1]
            if array[i] > stack[-1]

