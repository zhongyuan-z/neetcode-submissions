class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        check = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)): 
            while check and check[-1][1] < temperatures[i]: 
                idx, temp = check.pop()
                res[idx] = i - idx
            check.append([i, temperatures[i]])
        return res