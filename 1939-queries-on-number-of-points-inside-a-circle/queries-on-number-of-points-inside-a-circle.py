class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        
        # O(n2), O(n)
        res = []

        def dist(x1, x2, y1, y2):
            return ( (x1 - x2)**2 + (y1 - y2)**2 ) ** 0.5

        for x1, y1, r in queries:
            c = 0
            for x2, y2 in points:

                if dist(x1, x2, y1, y2) <= r:
                    c += 1
            res.append(c)
        
        return res