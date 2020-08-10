 def find132pattern(self, nums: List[int]) -> bool:
        k = 3
        is_true = False
        subs = []
        if len(nums) < 3:
            return is_true
        else:
            for i in range(0, 3):
                subs.append(nums[i])
                if len(subs) == 3:
                    print(subs)
                    if subs[0] < subs[1] > subs[2]:
                        is_true = True
            for i in range(k, len(nums)):
                subs.pop(0)
                subs.append(nums[i])
                if subs[0] < subs[1] > subs[2]:
                        is_true = True
                print(subs)
        
        return is_true
            

            def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        else:
          
            dicti = {}
            for k in range(0, len(nums)):
                if nums[k] not in dicti:
                    dicti[nums[k]] = [nums[k]]
                    print(dicti)
                for i in range(k + 1, len(nums)):
                    if len(dicti[nums[k]]) == 1:
                        if nums[i] > nums[k]:
                            dicti[nums[k]].append(nums[i])
                            print(dicti)
                    for j in range(i + 1, len(nums)):
                        if len(dicti[nums[k]]) == 2:
                            if nums[j] < nums[i] and nums[j] > nums[k]:
                                dicti[nums[k]].append(nums[j])
                                print(dicti)
                                
                if len(dicti[nums[k]]) == 3:
                    return True
                else:
                    return False

                print(dicti)
