class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[-p, s] for p, s in zip(position, speed)]
        time = []
        heapq.heapify(cars)
        for i in range(len(position)): 
            ps, sp = heapq.heappop(cars)
            temp = (target + ps) / sp
            check = time[-1] if time else float("-inf")
            t = max(temp, check)
            time.append(t)
        count = 1
        for j in range(1, len(time)): 
            if time[j] != time[j - 1]: 
                count += 1
        return count