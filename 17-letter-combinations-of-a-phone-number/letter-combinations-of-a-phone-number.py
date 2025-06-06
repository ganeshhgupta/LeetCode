from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        def dfs(i, li):
            if i == len(digits):
                res.append(li)
                return

            letters = map[digits[i]]
            for l in letters:
                dfs(i + 1, li + l)

        dfs(0, "")
        return res
