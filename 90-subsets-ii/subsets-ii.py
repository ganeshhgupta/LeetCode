class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        nums.sort()

        def dfs(i):

            #returns when last element in nums has been reached, irrespective of how many elements are in subset array
            #why? cause i will increment irrespective for whether append or pop is happening to subset array
            if i == len(nums):
                res.append(subset.copy())
                return

            #subset = [] -> [1] -> [1, 2] ..
            #                   -> [] -> [2] -> [2, 3]
            #                                -> [] -> [3] .. so on

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            
            #to eliminate duplicates
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            #backtracking by going on element back in the existing subset
            #subset.pop()
            dfs(i+1)

        dfs(0)
        return res