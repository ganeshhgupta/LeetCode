class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # O(logn), O(1)

        # Case 1: nums[mid] > nums[right]
        # mid is in the left sorted part, so rotation/minimum is on the right
        # move l = mid + 1

        # Case 2: nums[mid] <= nums[right]
        # right part is sorted, minimum is at mid or on the left
        # move r = mid

        # Case 3: Array is already sorted
        # nums[mid] < nums[right], handled by Case 2
        # keep shrinking left side until minimum is found

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r-l)// 2

            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid
        
        return nums[l]