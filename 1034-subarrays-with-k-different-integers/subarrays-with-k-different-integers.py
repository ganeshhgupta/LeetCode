class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(k):
            window = {}
            l = res = 0

            for r in range(len(nums)):
                if nums[r] not in window:
                    window[nums[r]] = 1
                else:
                    window[nums[r]] += 1

                while len(window) > k:
                    window[nums[l]] -= 1
                    if window[nums[l]] == 0:
                        del window[nums[l]]
                    l += 1

                res += (r - l + 1)

            return res
        
        return atMost(k) - atMost(k - 1)