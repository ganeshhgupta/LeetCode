class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                # Minimum is in left half (including mid)
                r = mid
            elif nums[mid] > nums[r]:
                # Minimum is in right half
                l = mid + 1
            else:
                # nums[mid] == nums[r], can't decide
                r -= 1

        return nums[l]
