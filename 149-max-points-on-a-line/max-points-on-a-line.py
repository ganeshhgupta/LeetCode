class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        ans = 2

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                # Vertical line
                if dx == 0:
                    slope = (1, 0)

                # Horizontal line
                elif dy == 0:
                    slope = (0, 1)

                else:
                    g = gcd(abs(dx), abs(dy))
                    dx //= g
                    dy //= g

                    # Keep dx positive
                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] += 1
                ans = max(ans, slopes[slope] + 1)

        return ans
