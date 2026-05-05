class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        left, right = 0, 0
        while i < j: 
            l = max(0, left - height[i])
            r = max(0, right - height[j])
            res += l + r
            left = max(left, height[i])
            right = max(right, height[j])
            if left < right: 
                i += 1
            else: 
                j -= 1
        return res