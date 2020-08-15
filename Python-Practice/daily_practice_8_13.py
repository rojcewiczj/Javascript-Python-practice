heights = [3,2,5,6,1,4,4]
# should print 10

def max_size(heights):
    print(heights)
    # dicti = {}
    stack = []
    # for i in range(0, len(heights)):
    #     right = []
    #     left = []
    #     for j in range(i + 1, len(heights)):
    #         if heights[j] > heights[i]:
    #             right.append(heights[j])
    #         else:
    #             break
    #     for k in reversed(range(0, i)):
    #         if heights[k] > heights[i]:
    #             left.append(heights[k])
    #         else:
    #             break
        
    #     both = []
    #     both.append(left)
    #     both.append(right)
    #     dicti[heights[i]] = both
    
    # print(dicti)
    # for num in dicti:
    #     size = num * (len(dicti[num][0]) + len(dicti[num][1]) + 1)
    #     dicti[num] = size
    
    # print(dicti)
    
        

    
    


max_size(heights)