class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        dist = [float("inf")] * n
        dist[0] = 0
        seen = set()
        res = 0

        for _ in range(n):
            i = min((i for i in range(n) if i not in seen),
                    key=lambda i: dist[i])

            seen.add(i)
            res += dist[i]

            for j in range(n):
                if j not in seen:
                    d = abs(points[i][0] - points[j][0]) + \
                        abs(points[i][1] - points[j][1])
                    dist[j] = min(dist[j], d)

        return res