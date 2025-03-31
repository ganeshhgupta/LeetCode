class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        #approach is to run dfs from the outer sides for both pacific and atlantic and keep dfsing innerwards and adding cells to set. If a cell is present in both pacific and atlantic set, add it to res.
        def outOfBounds(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols):
                return True
            return False

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or outOfBounds(r, c) or heights[r][c] < prevHeight):
                return
            visit.add((r, c))

            for dr, dc in dir:
                dfs(r + dr, c + dc, visit, heights[r][c])


        for c in range(cols):
            #checking if topmost row flows into pacific
            dfs(0, c, pacific, heights[0][c])
            #checking if bottomomst row flows into atlantic
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])

        for r in range(rows):
            #checking if leftmost row flows into pacific
            dfs(r, 0, pacific, heights[r][0])
            #checking if rightmost row flows into atlantic
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res