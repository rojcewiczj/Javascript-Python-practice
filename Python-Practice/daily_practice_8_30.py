array = [1,2,3,6,3,4,6,7,3,2,9,8]
rectangles = {}
i = 0
stack = []
ans = array[i]
for i in range(0, len(array)):
    if len(stack) == 0 or array[stack[-1]] <= array[i]:
        stack.append(i)
        i += 1
    else:
        height = array[stack.pop(-1)]
        print(stack[-1])
        print(i)
        if len(stack) != 0:
            size = height * (i- stack[-1] -1)
            print(size)
        elif len(stack) == 0:
            size = height * i
        if size > ans:
            ans = size
        print(stack)
        




    