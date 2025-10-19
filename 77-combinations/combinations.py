class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # O(C(n, k) * k), O(k)
        
        res = []
        def dfs(i, li):

            if len(li) == k:
                res.append(li.copy())
                return
            
            for j in range(i, n + 1):
                li.append(j)
                dfs( j + 1, li)
                li.pop()
            
            return
        
        dfs(1, [])
        return res
