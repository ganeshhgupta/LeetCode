class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        if max(nums) <= k and min(nums) != max(nums):
            return -1

        if len(nums) == 1 and nums[0] < k:
            return -1

        if k > min(nums):
             return -1

        count = len(set(nums))
        if min(nums) == k:
            count -= 1
        return count
