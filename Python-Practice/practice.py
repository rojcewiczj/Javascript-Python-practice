    stack = []
    i = 0
    maxis = [0] * len(h)
    while i < len(h):
        if len(stack) == 0 or h[i] >= h[stack[-1]]:
            stack.append(h[i])
            i += 1
        else:
            x = h[stack.pop(-1)]
            if len(stack) == 0:
                size = x * i
            else:
                size = x * (i - stack[-1] - 1)
            maxis[i-stack[-1] - 1] = size
    while len(stack) > 0:
        x = h[stack.pop(-1)]
        if len(stack) == 0:
            size = x * len(h)
        else:
            size = x * (len(h) - stack[-1]-1)
            maxis[i-stack[-1] -1] = size
    print(maxis)