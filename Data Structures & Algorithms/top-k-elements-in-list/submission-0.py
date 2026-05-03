class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums: 
            if num in hmap: 
                hmap[num] += 1
            else: 
                hmap[num] = 1
        stack = []
        for key, values in hmap.items(): 
            stack.append([-values, key])
        heapq.heapify(stack)
        res = []
        for i in range(k): 
            temp = heapq.heappop(stack)[1]
            res.append(temp)
        return res