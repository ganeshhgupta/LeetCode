class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # O(4ⁿ), O(4ⁿ)
        
        if not digits:
            return []
        
        map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        n = len(digits)
        res = []

        def dfs(i, li):
            if i == n:
                res.append(li)
                return

            for j in map[digits[i]]:
                dfs(i + 1, li + j)

        dfs(0, "")
        return res
