class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # O(2ⁿ · n), O(n)
        
        res = []
        def isPal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        def dfs(i, li) :

            if i == len(s):
                res.append(li.copy())

            for j in range(i, len(s)):
                if isPal(i, j):
                    dfs(j + 1, li + [s[i:j+1]])
        dfs(0, [])
        return res
