class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for i in range(len(s)): 
            if s[i] ==  ")": 
                if not q or q.pop() != "(": 
                    return False
            elif s[i] == "]": 
                if not q or q.pop() != "[": 
                    return False
            elif s[i] == "}" : 
                if not q or q.pop() != "{": 
                    return False
            else: 
                q.append(s[i])
        return True if not q else False