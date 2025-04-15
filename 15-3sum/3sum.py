class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        res = []
        n = len(nums)

        def twosumtwo(i, j, target):
            pairs = []
            left, right = i, j
            while left < right:
                curr = nums[left] + nums[right]
                if curr > target:
                    right -= 1
                elif curr < target:
                    left += 1
                else:
                    pairs.append([nums[left], nums[right]])
                    #skip duplicates for i and j
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            return pairs

        for k in range(n - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # skip duplicates for k

            two_sum_pairs = twosumtwo(k + 1, n - 1, target - nums[k])
            for pair in two_sum_pairs:
                res.append([nums[k]] + pair)

        return res
