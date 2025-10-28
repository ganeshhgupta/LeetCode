class Solution:
    def numTrees(self, n: int) -> int:

        # Catalan sequence: 1, 1, 2, 5, 14, 42, 132, 429, ...
        # O(n²), O(n)

        res = 1
        for i in range(n):
            res = res * 2 * (2 * i + 1) // (i + 2)
        return res

        '''
        The Catalan numbers show up in MANY problems:
        - Number of unique BSTs with n nodes (this problem!)
        - Number of valid parentheses combinations
        - Number of ways to triangulate a polygon
        - Number of paths in a grid (without crossing)
        - Number of ways to arrange items in a stack

        Formula: C(n) = C(0)*C(n-1) + C(1)*C(n-2) + ... + C(n-1)*C(0)
        '''