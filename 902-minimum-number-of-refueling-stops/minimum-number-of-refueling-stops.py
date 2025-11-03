class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        # greedy: O(n log n), O(n), n = stations
        
        stations.append((target, float('inf')))
        mh = []

        prev = 0
        res = 0

        for location, capacity in stations:

            startFuel -= (location - prev)

            while mh and startFuel < 0:
                startFuel += -heapq.heappop(mh)
                res += 1
            
            if startFuel < 0:
                return -1
            
            heapq.heappush(mh, -capacity)
            prev = location
        
        return res