class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        #https://www.youtube.com/watch?v=oLEKpPXUgm4

        n = len(nums)
        pos = nums.index(k)

        count = defaultdict(int)

        bal = 0

        for i in range(pos, n):
            num = nums[i]

            bal += 1 if num > k else ( -1 if num < k else 0)
            count[bal] += 1

        res = 0
        bal = 0

        for i in reversed(range(pos + 1)):
            num = nums[i]

            bal += 1 if num > k else ( -1 if num < k else 0)
            res += count[-bal] #odd length subarrays
            res += count[-bal + 1] #even length subarrays

        return res