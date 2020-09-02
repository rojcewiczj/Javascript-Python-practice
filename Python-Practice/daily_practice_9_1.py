array = [4,3,1,3,6,2,5,6]
ans = 0
stack = []
i = 0
while i < len(array):
    if len(stack) == 0 or array[stack[-1]] <= array[i]:
        stack.append(i)
        i += 1
    else:
        height = array[stack.pop(-1)]
        if len(stack) > 0:
            size = height * (i - stack[-1] -1)
        else:
            size = height * i
        if size < ans:
            ans = size
while len(stack) > 0:
    height = array[stack.pop(-1)]
    if len(stack) > 0:
        size = height * (len(array) - stack[-1] -1)
    else:
        size = height * len(array)
    if size < ans:
        ans = size
        
print(ans)