# def wiggleSort(self, nums: List[int]) -> None:
#     rev_nums = []
#     new_nums = list(nums)
#     new_nums.sort()
        
#     for num in reversed(new_nums):
#         rev_nums.append(num)
        
#     mid = len(rev_nums) // 2
#     print(mid)
#     print(rev_nums)
#     print(nums)
        
#     j = 1
        
#     for i in range(0, mid):
#         nums[j] = rev_nums[i]
#         j += 2
#     print(nums)
#     j = 0
        
        
#     for i in range(mid, len(nums)):
#         nums[j] = rev_nums[i]
#         j += 2  
        

def wiggle_sort(array):

    for index in range (0, len(array) -1):
        if (index + 1) % 2 == 0:
            if array[index + 1] > array[index]:
                next_num = array[index+1]
                current_num = array[index]
                array[index + 1] = current_num
                array[index] = next_num
                
    for index in range (0, len(array) -1):
        if (index + 1) % 2 == 1:
            if array[index + 1] < array[index]:
                next_num = array[index+1]
                current_num = array[index]
                array[index + 1] = current_num
                array[index] = next_num
    
    print(array)

wiggle_sort([1,4,6,5,3,2,9,10,3])