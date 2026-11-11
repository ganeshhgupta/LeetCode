class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:

        # Sort points by X coordinate
        sorted_x = sorted(points, key=lambda p: p[0])

        # Sorted X values for binary search
        xs = [p[0] for p in sorted_x]

        ans = []

        for cx, cy, r in queries:
            # Find points within horizontal bounding range
            left = bisect.bisect_left(xs, cx - r)
            right = bisect.bisect_right(xs, cx + r)

            count = 0

            # Check actual circular distance
            for x, y in sorted_x[left:right]:
                if (x - cx)**2 + (y - cy)**2 <= r**2:
                    count += 1

            ans.append(count)

        return ans
