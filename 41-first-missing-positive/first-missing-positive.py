class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if not nums or 1 not in nums:
            return 1

        #convert all negatives and zeroes and numbers greater than len(nums) to 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        #now that we don't have any negatives in the array,
        #for every num at ith index, flip the num-th index to negative

        for i, num in enumerate(nums):
            to_change = nums[abs(num) - 1]

            if to_change > 0:
                nums[abs(num) - 1] *= -1

        #after above operation is done, the first positive element encountered (+1) would be the answer

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        #else, answer would be len(nums) + 1

        return len(nums) + 1
