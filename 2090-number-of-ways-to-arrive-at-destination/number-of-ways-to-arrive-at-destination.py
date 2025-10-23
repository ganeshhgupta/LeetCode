from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        MOD = 10 ** 9 + 7

        mh = [(0, 0)]
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        path_count = [0] * n
        path_count[0] = 1

        while mh:
            cost, node = heappop(mh)

            if cost > min_cost[node]:
                continue

            for nei, w in adj[node]: 
                if cost + w < min_cost[nei]:
                    min_cost[nei] = cost + w
                    path_count[nei] = path_count[node]
                    heappush(mh, (min_cost[nei], nei))

                elif cost + w == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD

        return path_count[n-1]
