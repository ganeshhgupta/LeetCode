class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0: -1}
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            mod = total % k if k != 0 else total
            
            if mod in mods:
                if i - mods[mod] > 1:
                    return True
            else:
                mods[mod] = i

        return False
