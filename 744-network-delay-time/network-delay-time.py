class Solution:
    def networkDelayTime(self, times, n, k):

        # TC: O((V + E) log V), SC: O(V + E)

        # Build a directed weighted graph: u -> v with travel time w.
        # Run Dijkstra from k to find the shortest time to reach every node.
        # The answer is the maximum shortest time among all nodes.
        # If any node is unreachable, return -1.

        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        q = [(0, k)]
        v = set()
        dist = 0

        while q:
            time, node = heapq.heappop(q)

            if node in v:
                continue

            v.add(node)
            dist = max(dist, time)

            for nei, nei_time in adj[node]:
                heapq.heappush(q, (time + nei_time, nei))

        return dist if len(v) == n else -1

