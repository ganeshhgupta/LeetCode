class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(i, li):
            if i == len(nums):
                res.append(li.copy())
                return 
            
            dfs(i+1, li+[nums[i]])
            dfs(i+1, li)
        dfs(0, [])
        return res