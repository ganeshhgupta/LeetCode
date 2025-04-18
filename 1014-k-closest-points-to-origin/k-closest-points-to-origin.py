class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def man(x, y):
            return (sqrt(x**2 + y**2))

        dist_map = defaultdict(list)

        for x, y in points:
            dist = man(x, y)
            dist_map[dist].append([x, y])

        result = []

        for dist in sorted(dist_map.keys()):
            for pt in dist_map[dist]:
                result.append(pt)
                if len(result) == k:
                    return result

        return result
