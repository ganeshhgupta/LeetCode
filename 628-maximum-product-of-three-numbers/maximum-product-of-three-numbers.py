class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(nums)
        print(sorted_nums)
        print(nums[-1] * nums[-2] * nums[-3])
        print(nums[0] * nums[1] * nums[-1])
        return max(sorted_nums[-1] * sorted_nums[-2] * sorted_nums[-3], sorted_nums[0] * sorted_nums[1] * sorted_nums[-1])