class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = -1
        while l <= r: 
            mid = (l + r) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: 
                row = mid
                break
            elif matrix[mid][0] > target: 
                r = mid - 1
            else: 
                l = mid + 1
        if row == -1: 
            return False
        ln, rn = 0, len(matrix[0]) - 1
        while ln <= rn:  
            mid = (ln + rn) // 2
            if matrix[row][mid] > target:
                rn = mid - 1
            elif matrix[row][mid] < target: 
                ln = mid + 1
            else: 
                return True
        return False