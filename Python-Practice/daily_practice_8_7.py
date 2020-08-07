def wiggleSort(self, nums: List[int]) -> None:
    rev_nums = []
    new_nums = list(nums)
    new_nums.sort()
        
    for num in reversed(new_nums):
        rev_nums.append(num)
        
    mid = len(rev_nums) // 2
    print(mid)
    print(rev_nums)
    print(nums)
        
    j = 1
        
    for i in range(0, mid):
        nums[j] = rev_nums[i]
        j += 2
    print(nums)
    j = 0
        
        
    for i in range(mid, len(nums)):
        nums[j] = rev_nums[i]
        j += 2  
        