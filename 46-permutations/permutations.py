class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def dfs(i, li):
            nonlocal res

            if i == n:
                res.append(li.copy())
                return
            
            for j in range(len(li) + 1):
                li.insert(j, nums[i])
                dfs(i + 1, li)
                li.pop(j)
            
            return
        
        dfs(0, [])
        return res