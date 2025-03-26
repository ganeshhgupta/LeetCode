class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        #flatten it, sort it, if every element of array % x == the same value, it is doable
        mod = grid[0][0] % x
        steps = 0
        flattened = [grid[m][n] for m in range(len(grid)) for n in range(len(grid[m])) if grid[m][n] % x == mod]

        if len(flattened) != len(grid) * len(grid[0]):
            return -1

        flattened_sorted = sorted(flattened)
        median = flattened_sorted[len(flattened_sorted)//2]

        #find jumps from every value to median
        for i in flattened_sorted:
            steps += (abs(median - i)//x)

        return steps