class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Skip duplicates: only proceed if the previous element is not used and it's a duplicate
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                dfs(path + [nums[i]], used)
                used[i] = False

        used = [False] * len(nums)
        dfs([], used)
        return res
