array =[[2,3],[4,5],[1,3],[5,6]]

def re_order(arr):
    dicti = {}
    for ar in arr:
        dicti[ar[0]] = ar[1]
    
    print(dicti)
re_order(array)