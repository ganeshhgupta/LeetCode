class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i, sum):
            if sum == target:
                res.append(subset.copy())  # Found a valid combination, so add it to result
                return
            if sum > target or i >= len(candidates):  # If sum exceeds target or no candidates left
                return

            # Include the current candidate (allowing reuse)
            subset.append(candidates[i])
            dfs(i, sum + candidates[i])  # Stay at the same index to reuse the current candidate

            # Backtrack: remove the last added element
            subset.pop()

            # Explore the next candidate (move to the next index)
            dfs(i + 1, sum)

        dfs(0, 0)
        return res
