class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(piles, rate): 
            total = 0
            for p in piles: 
                total += math.ceil(p / rate)
            return total
        l, r = 1, max(piles)
        need = 0
        while l <= r: 
            mid = (l + r) // 2
            t = time(piles, mid)
            if t > h: 
                l = mid + 1
            else:
                need = mid
                r = mid - 1
        return need
            