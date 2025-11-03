class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        
        smallest = min(nums)
        largest = max(nums)

        if largest - smallest + 1 > len(nums):
            return [i for i in range(smallest, largest + 1) if i not in nums]

        for i in range(len(nums)):
            nums[i] = nums[i] - smallest + 1

        i = 0
        while i < len(nums):
            idx = abs(nums[i]) - 1
            if 0 <= idx < len(nums) and nums[idx] > 0:
                nums[idx] = -nums[idx]
            i += 1
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + smallest)
        
        return res
