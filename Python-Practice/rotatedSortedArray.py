nums = [4,5,6,7,0,1,2]
target = 1

def find(array, target):
    left = 0
    right = len(nums) -1
   
    while(left <= right):
        mid = (left + right) // 2
        if(array[mid] == target):
            return mid
        
        if array[left] < array[mid]:
            if target > array[left] and target < array[mid]:
                right = mid -1
            else:
                left = mid + 1
        else:
            if target < array[right] and target > array[mid]:
                left = mid +1
            else:
                right = mid - 1
    

    return -1



print(find(nums, target))



