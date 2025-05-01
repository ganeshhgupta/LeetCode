class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        res = []
        c = list(currentState)

        def dfs(i):
            if i >= len(c) - 1:
                return
            if c[i] == '+' and c[i + 1] == '+':
                c[i], c[i + 1] = '-', '-'
                res.append("".join(c))

                c[i], c[i + 1] = '+', '+'
            dfs(i + 1)

        dfs(0)
        return res
