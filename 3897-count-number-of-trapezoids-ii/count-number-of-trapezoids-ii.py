class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        res = 0
        
        slopes  = Counter()
        lines = Counter()
        midpoints = Counter()
        midlines = Counter()

        for (x1, y1) , (x2, y2) in combinations(points, 2):

            dy = y2 - y1
            dx = x2 - x1

            g = gcd(dy, dx)

            dy = dy // g 
            dx = dx // g

            if (dy, dx) < (0, 0):
                dy, dx = - dy, - dx
            
            c = dx * y1 - dy * x1

            slopes[dy, dx] += 1
            lines[dy, dx, c] += 1
            midpoints[x1 + x2, y1 + y2] += 1
            midlines[x1 + x2, y1 + y2, dy, dx, c ] += 1

        res += sum(comb(v, 2) for v in slopes.values())
        res -= sum(comb(v, 2) for v in lines.values())
        res -= sum(comb(v, 2) for v in midpoints.values())
        res += sum(comb(v, 2) for v in midlines.values())

        return res
