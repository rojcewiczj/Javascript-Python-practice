def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialmatch = targetSum - num
        if potentialMatch in nums:
            return [potentialmatch, num]
        else:
            nums[num] = True
    return

