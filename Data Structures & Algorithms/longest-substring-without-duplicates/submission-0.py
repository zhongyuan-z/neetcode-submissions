class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        q = deque()
        res = 0
        for i in range(len(s)): 
            while s[i] in visit: 
                temp = q.popleft()
                visit.remove(temp)
            q.append(s[i])
            visit.add(s[i])
            res = max(res, len(q))
        return res