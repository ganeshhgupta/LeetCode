class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods = {0: -1}
        total = 0
        k = 1 if k == 0 else k
        for i, num in enumerate(nums):
            total += num
            mod = total % k
            
            if mod in mods:
                if i - mods[mod] > 1:
                    return True
            else:
                mods[mod] = i

        return False
