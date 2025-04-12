class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot_i = -1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_i = i
                break

        if pivot_i == -1: #list is in desc
            nums.reverse()
            return

        print(pivot_i)

        #find first element from rhs > pivot:
        for i in range(len(nums) - 1, pivot_i, -1):
            if nums[i] > nums[pivot_i]:
                print(i)
                nums[i], nums[pivot_i] = nums[pivot_i], nums[i] 
                break

        nums[pivot_i + 1:] = sorted(nums[pivot_i + 1:])