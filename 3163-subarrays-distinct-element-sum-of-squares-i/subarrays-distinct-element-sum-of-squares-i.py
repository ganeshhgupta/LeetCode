class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0

        def dfs(i, li, started):
            nonlocal res
            if i == n:
                return

            li = li + [nums[i]]
            res += len(set(li)) ** 2
            dfs(i + 1, li, True)

            if not started:
                dfs(i + 1, [], False)

        dfs(0, [], False)
        return res