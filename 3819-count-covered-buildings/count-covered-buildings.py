class Solution:
    def countCoveredBuildings(self, n: int, b: List[List[int]]) -> int:
      
        # O(n), O(n)
        # for every x-coord find min and max y, vice versa
        
        res = 0

        x_min = defaultdict(lambda: math.inf)
        x_max = defaultdict(lambda: -math.inf)
        y_min = defaultdict(lambda: math.inf)
        y_max = defaultdict(lambda: -math.inf)

        for x, y in b:
            x_min[y] = min(x_min[y], x)
            y_min[x] = min(y_min[x], y)
            x_max[y] = max(x_max[y], x)
            y_max[x] = max(y_max[x], y)
        
        for x, y in b:
            if y_min[x] < y < y_max[x] and x_min[y] < x < x_max[y]:
                res += 1
        
        return res

    

    