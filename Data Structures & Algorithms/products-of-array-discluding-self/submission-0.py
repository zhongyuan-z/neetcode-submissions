class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        num = 1
        for i in range(len(nums)): 
            res.append(num)
            num *= nums[i]
        num = 1
        for i in range(len(nums) - 1, -1, -1): 
            res[i] *= num
            num *= nums[i]
        return res