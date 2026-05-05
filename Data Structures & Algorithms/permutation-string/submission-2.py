class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = {}
        for s in s1: 
            if s in hmap: 
                hmap[s] += 1
            else: 
                hmap[s] = 1
        total = len(hmap)
        check = {}
        count = 0
        for i in range(len(s2)): 
            if s2[i] in hmap: 
                j = i
                while j < len(s2) and s2[j] in hmap:
                    check[s2[j]] = 1 + check.get(s2[j], 0)
                    if check[s2[j]] == hmap[s2[j]]: 
                        count += 1
                    elif check[s2[j]] > hmap[s2[j]]: 
                        break
                    if count == total: 
                        return True
                    j += 1
            check = {}
            count = 0
        return False
            
