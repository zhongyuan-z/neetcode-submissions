class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        max_count = 0
        hmap = defaultdict(int)
        for right in range(len(s)): 
            hmap[s[right]] += 1
            max_count = max(max_count, hmap[s[right]])
            while right - left + 1 - max_count > k:  
                hmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res