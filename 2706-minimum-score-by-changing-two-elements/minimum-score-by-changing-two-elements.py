class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        # O(1), O(1)

        n = len(nums)

        if n <= 3:
            return 0

        nums.sort()

        return min(
            nums[n - 1] - nums[2],
            nums[n - 2] - nums[1],
            nums[n - 3] - nums[0]
        )
