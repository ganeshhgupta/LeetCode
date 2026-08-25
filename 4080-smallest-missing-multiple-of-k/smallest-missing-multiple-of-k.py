class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        nums = set(nums)
        i = 2
        target = k
        while True:

            if target not in nums:
                #print(target)
                return target
            else:
                target = k * i
                i += 1
