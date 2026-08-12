class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        # Dijkstra's

        adj = defaultdict(list)
        for edges , c in zip(edges, succProb):
            a, b = edges
            adj[a].append((b, c))
            adj[b].append((a, c))
        
        mh = [(-1, start_node)] # max-heap (add -ve sign) ; highest probability = 1
        v = set()

        while mh:
            prob, node = heapq.heappop(mh)
            v.add(node)

            if node == end_node:
                return -prob
            
            for nei, nei_prob in adj[node]:

                if nei not in v:
                    heapq.heappush(mh, (prob * nei_prob, nei))
        
        return 0



