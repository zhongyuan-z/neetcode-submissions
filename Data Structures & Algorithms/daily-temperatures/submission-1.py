class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        check = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures): 
            while check and check[-1][1] < temp: 
                idx, t = check.pop()
                res[idx] = i - idx
            check.append([i, temp])
        return res