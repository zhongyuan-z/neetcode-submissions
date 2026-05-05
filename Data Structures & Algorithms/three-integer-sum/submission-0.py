class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        visit = set()
        for i in range(len(nums)): 
            target = nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k: 
                if target + nums[j] + nums[k] == 0: 
                    check = (target, nums[j], nums[k])
                    if check not in visit: 
                        res.append([target, nums[j], nums[k]])
                        visit.add((target, nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif target + nums[j] + nums[k] < 0: 
                    j += 1
                else: 
                    k -= 1
        return res