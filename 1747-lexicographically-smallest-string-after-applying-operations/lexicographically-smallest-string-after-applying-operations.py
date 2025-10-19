class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        # O(m * n), O(m * n)
        
        n = len(s)

        added = {}
        for i in range(10):
            added[str(i)] = str((i + a) % 10)

        def add(s):
            res = ''
            for i in range(n):
                res += s[i] if i % 2 == 0 else added[s[i]]
            return res
        
        def rotate(s):
            return s[n-b:] + s[:n-b]

        visited = set()

        def dfs(s):
            if s in visited:
                return
            
            visited.add(s)
            dfs(add(s))
            dfs(rotate(s))
            return
        
        dfs(s)
        return min(visited)