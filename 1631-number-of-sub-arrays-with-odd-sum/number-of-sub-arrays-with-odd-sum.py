class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        
        n = len(arr)
        even = 1
        odd = 0
        res = 0
        curr = 0
        MOD = 10**9 + 7

        for num in arr:
            curr += num

            if curr % 2:
                res += even
                odd += 1
            else:
                res += odd
                even += 1

        return res % MOD