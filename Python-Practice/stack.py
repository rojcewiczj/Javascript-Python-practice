
sequence= "(()"
stack = []

for parathese in sequence:
    if parathese == "(":
        stack.append(parathese)
    elif len(stack) > 0:
        stack.pop(-1)
    else:
        print("false")

if len(stack) > 0:
    print("false")
        