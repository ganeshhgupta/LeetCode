class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # O(2ⁿ), O(n)
        res = []
        def dfs(i, li):                 # without li.pop()
            if i == len(nums):
                res.append(li)
                return
            
            dfs(i + 1, li + [nums[i]])  # directly change while passing through fn
            dfs(i + 1, li)

        def dfs(i, li):
            if i == len(nums):
                res.append(li.copy())
                return
            
            li.append(nums[i])              # include nums[i]
            dfs(i + 1, li)
            li.pop()                        # backtrack
            dfs(i + 1, li)                  # exclude nums[i]

        dfs(0, [])
        return res