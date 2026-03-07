class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # O(ElogV), O(E^2), Dijksra's

        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        mh = [(0, k)]
        v = set()
        t = 0
        while mh:
            w1, n1 = heapq.heappop(mh)
            if n1 in v:
                continue
            v.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in v:
                    heapq.heappush(mh, (w1 + w2, n2))

        return t if len(v) == n else -1