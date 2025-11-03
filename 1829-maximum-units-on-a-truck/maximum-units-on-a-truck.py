class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # O(n), O(n)

        heap = [(-units, size) for size, units in boxTypes] # max-heap
        heapq.heapify(heap)
        
        res = 0
        
        while truckSize > 0 and heap:
            neg_units, size = heapq.heappop(heap)
            units = -neg_units
            
            take = min(size, truckSize)
            res += take * units
            truckSize -= take
        
        return res
