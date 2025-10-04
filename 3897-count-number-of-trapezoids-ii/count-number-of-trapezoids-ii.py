class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        m = Counter()
        lines = Counter()
        mdpt = Counter()
        mdln = Counter()

        for (x1, y1), (x2, y2) in combinations(points, 2):
            dy, dx = y2-y1, x2-x1
            g = gcd(dy, dx) # to reduce the fraction
            dy, dx = dy // g, dx // g
            if dx < 0 or (dx == 0 and dy < 0):
                dy, dx = -dy, -dx

            c = dx * y1 - dy * x1
            m[dy, dx] += 1
            lines[dy, dx, c] += 1
            mdpt[y1+y2, x1+x2] += 1
            mdln[y1+y2, x1+x2, dy, dx, c] += 1

        res = sum(comb(v, 2) for v in m.values()) # add all same slopes
        res -= sum(comb(v, 2) for v in lines.values()) # minus all collinear lines
        res -= sum(comb(v, 2) for v in mdpt.values()) # minus extra lines with same midpoint (paralellograms) (double-counted)
        res += sum(comb(v, 2) for v in mdln.values()) # add back collinear diagonals (over-subtracted)

        return res