class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        need = 0
        while l <= r: 
            mid = (l + r) // 2
            t = 0
            for i in range(len(piles)): 
                t += math.ceil(piles[i] / mid)
            if t > h: 
                l = mid + 1
            else:
                need = mid
                r = mid - 1
        return need
            