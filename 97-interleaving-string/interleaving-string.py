class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # bottom up backtrack
        # O(l1·l2), O(l1·l2)
        
        l1, l2, l3 = len(s1), len(s2), len(s3)

        if l1 + l2 != l3:
            return False

        cache = {}

        def dfs(p1, p2, p3):
            if p3 == l3:
                return p1 == l1 and p2 == l2

            if (p1, p2) in cache:
                return cache[(p1, p2)]
            
            res = False

            if p1 < l1 and s1[p1] == s3[p3]:
                res = dfs( p1 + 1, p2, p3 + 1)
            
            if not res and p2 < l2 and s2[p2] == s3[p3]:
                res = dfs(p1, p2 + 1, p3 +1)
            
            cache[(p1, p2)] = res
            return res
        
        return dfs(0, 0, 0)

            
            