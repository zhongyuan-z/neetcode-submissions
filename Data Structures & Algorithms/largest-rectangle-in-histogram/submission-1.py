class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights): 
            temp = i
            while area and area[-1][1] >= h: 
                idx, height = area.pop()
                max_area = max(max_area, height * (i - idx))
                temp = idx
            area.append([temp, h])
        return max_area
