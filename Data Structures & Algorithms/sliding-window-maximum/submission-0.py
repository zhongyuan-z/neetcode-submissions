class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        q = deque()
        res = []
        for i in range(len(nums)): 
            if len(q) == k: 
                temp = q.popleft()
                hmap[temp] -= 1
                if hmap[temp] == 0: 
                    del hmap[temp]
            q.append(nums[i])
            hmap[nums[i]] = 1 + hmap.get(nums[i], 0)
            res.append(max(hmap))
        return res[k-1:]
            