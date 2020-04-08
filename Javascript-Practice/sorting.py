def merge( arrA, arrB ):
    i=0
    j=0
    len1 = len(arrA)
    len2 = len(arrB)
    merged_arr = []

    while((i < len1) and (j < len2)):
        if(arrA[i] < arrB[j]):
            merged_arr.append(arrA[i])
            i = i + 1
        else:
            merged_arr.append(arrB[j])
            j = j + 1
    while(i < len1):
        merged_arr.append(arrA[i])
        i = i + 1
    while (j < len2):
        merged_arr.append(arrB[j])
        j = j + 1

    

    # TO-DO
  
    
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

    # TO-DO
    # for i, num in enumerate(arr): 
    #     try: 
    #         if arr[i+1] < num: 
    #             arr[i] = arr[i+1] 
    #             arr[i+1] = num 
    #             merge_sort(arr) 
    #     except IndexError: 
    #         pass



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
