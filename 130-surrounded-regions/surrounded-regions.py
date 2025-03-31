class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #approach: all "O"s at end edges and all the "O"s directly connected to them (not diagonally) won't be changed
        def outOfBounds(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols):
                return True
            return False

        def dfs(r, c):
            if ((r, c) in visited or outOfBounds(r, c) or board[r][c] == "X"):
                return
            visited.add((r, c))

            for dr, dc in dir:
                dfs(r + dr, c + dc)


        for c in range(cols):
            #dfsing from top
            dfs(0, c)
            #dfsing from bottom
            dfs(rows - 1, c)

        for r in range(rows):
            #dfsing from left 
            dfs(r, 0)
            #dfsing from right
            dfs(r, cols - 1)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"

        #return grid