class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = []
        count = 1
        for i in range(len(heights)): 
            h = heights[i]
            l, r = i - 1, i + 1
            while 0 <= l or r < len(heights): 
                if 0 <= l: 
                    if heights[l] >= h: 
                        count += 1
                        l -= 1
                    else: 
                        l = -1
                if r < len(heights): 
                    if heights[r] >= h: 
                        count += 1
                        r += 1
                    else: 
                        r = len(heights)
            area.append(h * count)
            count = 1
        return max(area)
