class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        visit = set(nums)
        used = set()
        res = 1
        for num in nums: 
            if num in used: 
                continue
            if num - 1 in visit: 
                temp = num
                while temp - 1 in visit:
                    temp -= 1
                count = 0
                while temp in visit: 
                    used.add(temp)
                    count += 1
                    temp += 1
                res = max(res, count)
        return res

