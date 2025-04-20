class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):
            
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1) #include nums[i] and go on to explorig subsets which contain nums[i]

            subset.pop()
            dfs(i+1) #exclude nums[i] and go on to explorig subsets which don't contain nums[i]

        dfs(0)
        return res