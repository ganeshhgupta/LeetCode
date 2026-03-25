class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        # O(m.n), O(m+n)
        row_sums = []
        col_sums = [0] * len(grid[0])

        for i in range(len(grid)):
            row_sums.append(sum(grid[i]))
            for j in range(len(grid[0])):
                col_sums[j] += grid[i][j]

        total = sum(row_sums)

        curr = 0
        for i in range(len(grid) - 1):
            curr += row_sums[i]
            if curr * 2 == total:
                return True

        curr = 0
        for j in range(len(grid[0]) - 1):
            curr += col_sums[j]
            if curr * 2 == total:
                return True

        return False