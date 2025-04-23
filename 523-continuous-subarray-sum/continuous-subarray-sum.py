class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        map = {0: -1}
        pref = 0
        k = 1 if k == 0 else k
        
        for i, num in enumerate(nums):
            pref += num
            mod = pref % k
            
            if mod in map:
                if i - map[mod] > 1:
                    return True
            else:
                map[mod] = i

        return False
