class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs: 
            temp = [0] * 26
            for i in range(len(s)): 
                temp[ord(s[i]) - ord("a")] += 1
            temp = tuple(temp)
            if temp in hmap: 
                hmap[temp].append(s)
            else: 
                hmap[temp] = [s]
        return list(hmap.values())