class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        # djikstra 

        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))

        MOD = 10 ** 9 + 7

        mh = [(0,0)]
        min_cost = [float('inf')] * n
        path_count = [0] * n
        path_count[0] = 1

        while mh:
            cost, node = heappop(mh)

            for nei_cost, nei in adj[node]:
                
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heappush(mh, (min_cost[nei], nei))

                elif cost + nei_cost == min_cost[nei]:
                    path_count[nei] = ( path_count[nei] + path_count[node] ) % MOD

        return path_count[n-1]








