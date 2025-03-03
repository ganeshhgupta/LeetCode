class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):

            #returns when last element in nums has been reached, irrespective of how many elements are in subset array
            #why? cause i will increment irrespective for whether append or pop is happening to subset array
            if i >= len(nums):
                res.append(subset.copy())
                return

            #subset = [] -> [1] -> [1, 2] ..
            #                   -> [] -> [2] -> [2, 3]
            #                                -> [] -> [3] .. so on
            subset.append(nums[i])
            dfs(i+1)

            #backtracking by going on element back in the existing subset
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res