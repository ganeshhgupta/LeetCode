class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # O(n.logn), O(n^2)
        n = len(points)
        v = set()
        mh = [(0, 0)]  # (cost, point_index)
        res = 0
        
        while len(v) < n:
            cost, i = heapq.heappop(mh)
            if i in v:
                continue
            
            v.add(i)
            res += cost
            
            # For each unvisited neighbor, calculate distance and push to heap
            for j in range(n):
                if j not in v:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(mh, (dist, j))
        
            # Loop continues until all points are connected
            
        return res
