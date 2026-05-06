class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n: 
            return ""
        hmap = {}
        for ch in t: 
            hmap[ch] = 1 + hmap.get(ch, 0)
        l = 0
        res = ""
        length = float("inf")
        have, need = 0, len(hmap)
        for r in range(len(s)): 
            if s[r] in hmap: 
                hmap[s[r]] -= 1
                if hmap[s[r]] == 0: 
                    have += 1
            while have == need: 
                if r - l + 1 < length: 
                    length = r - l + 1
                    res = s[l : r + 1]
                temp = s[l]
                if temp in hmap: 
                    hmap[temp] += 1
                    if hmap[temp] > 0: 
                        have -= 1
                l += 1
        return res