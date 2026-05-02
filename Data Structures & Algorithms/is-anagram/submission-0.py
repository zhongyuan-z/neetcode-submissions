class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        for ch in s: 
            if ch in hmap: 
                hmap[ch] += 1
            else: 
                hmap[ch] = 1
        count = 0
        for c in t: 
            if c not in hmap: 
                return False
            hmap[c] -= 1
            if hmap[c] < 0: 
                return False
            if hmap[c] == 0: 
                count += 1
        return True if len(hmap) == count else False