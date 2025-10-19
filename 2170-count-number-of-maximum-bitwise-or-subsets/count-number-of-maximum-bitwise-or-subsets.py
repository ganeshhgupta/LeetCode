class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        # O(2n), O(n)
        
        max_or = 0
        res = 0

        for i in nums:
            max_or |= i

        def dfs(i, cur_or):
            nonlocal res, max_or

            if i == len(nums):
                res += 1 if cur_or == max_or else 0
                return
            
            dfs(i + 1, cur_or | nums[i])
            dfs(i + 1, cur_or)
        
        dfs(0, 0)
        return res