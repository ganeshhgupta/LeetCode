class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
      
        # djikstra (which is just bfs + minheap)
        
        adj = defaultdict(list)

        for i, j, w in edges:
            adj[i].append((j, w))
            adj[j].append((i, w))

        def dijkstra(src):
            mh = [(0, src)]
            dist = [float('inf')] * n
            dist[src] = 0
            
            while mh:
                d, node = heappop(mh)
                
                if d > dist[node]:
                    continue
                
                for nei, weight in adj[node]:
                    new_dist = d + weight
                    if new_dist < dist[nei] and new_dist <= distanceThreshold:
                        dist[nei] = new_dist
                        heappush(mh, (new_dist, nei))
            
            return sum(1 for d in dist if d <= distanceThreshold) - 1

        res, min_count = 0, float('inf')
        for i in range(n):
            count = dijkstra(i)
            if count <= min_count:
                res, min_count = i, count
        
        return res