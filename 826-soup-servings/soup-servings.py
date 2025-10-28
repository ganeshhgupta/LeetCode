class Solution:
    def soupServings(self, n: int) -> float:
        
        # O(n²), O(n²)
        
        if n >= 5000:
            return 1.0

        serves = [[100,0], [75,25], [50,50], [25,75]]
        cache = {}

        def dfs(a, b):

            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1.0
            
            if b <= 0:
                return 0.0
            
            if (a, b) in cache:
                return cache[(a, b)]
            
            prob = 0.0
            for serve_a, serve_b in serves:
                prob += 0.25 * dfs( a - serve_a, b - serve_b)
            
            cache[(a, b)] = prob
            return prob
        
        return dfs(n, n)
