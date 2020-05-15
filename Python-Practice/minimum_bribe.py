def minimumBribes(q):
    dictionary = {}
    count = 0
    diff = 0
    too_chaotic = False
    for index, num in enumerate(q):
    #    print("new spot: ", index + 1,"original spot: " , num)
       if num > index + 1:
         diff = num - (index + 1)
         if diff > 2:
            too_chaotic = True
         count += diff
    
    if too_chaotic == False:
        print(count)
    else:
        print("Too chaotic")