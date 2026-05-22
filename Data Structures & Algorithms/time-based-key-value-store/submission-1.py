class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap: 
            self.hmap[key].append([timestamp, value])
        else: 
            self.hmap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hmap: 
            l, r = 0, len(self.hmap[key]) - 1
            while l < r: 
                mid = (l + r + 1) // 2
                if self.hmap[key][mid][0] <= timestamp: 
                    l = mid
                else: 
                    r = mid - 1
            return self.hmap[key][l][1] if self.hmap[key][l][0] <= timestamp else ""
        else: 
            return ""
