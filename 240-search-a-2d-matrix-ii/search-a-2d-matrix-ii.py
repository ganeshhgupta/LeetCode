class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # TC: O(N + M), SC: O(1)

        # Staircase from top-right: that cell is max of its row, min of its column.
        # So cur > target kills column j (all below are bigger); cur < target kills row i.
        # Each step drops a full row or column => O(N + M) time, O(1) space.

        N, M = len(matrix), len(matrix[0])
        i, j = 0, M - 1

        while i < N and j >= 0:

            cur = matrix[i][j]

            if cur == target:
                return True
                
            elif cur > target:
                j -= 1   # whole column j below is >= cur > target
            else:
                i += 1   # whole row i left of j is <= cur < target

        return False