class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        sub =[]
        for i in range(0, len(nums)):
            subs.append([nums[i]])
            if i > 0:
                current = len(subs) -1 
                for j in range(1, current):
                    for num in subs[j]:
                        sub.append(num)
                    sub.append(nums[i])
                    subs.append(sub)
                    sub = []
                    
                
           
            
            
            
        
        return subs