class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        # O(n log n), O(n)
        n = len(s)
        mod = 2**63 - 1
        nums = [ord(c) - ord('a') for c in s]
        print(nums)

        def dup(L):
            h = 0
            for i in range(L):
                h = (h * 26 + nums[i]) % mod
            seen = {h}
            baseL = pow(26, L, mod)
            for i in range(L, n):
                h = (h * 26 - nums[i - L] * baseL + nums[i]) % mod
                if h in seen:
                    return i - L + 1  # return starting index
                seen.add(h)
            return -1

        l, r = 1, n
        res_start = 0
        res_len = 0

        while l <= r:
            mid = l + (r - l) // 2
            candidate = dup(mid)
            if candidate != -1:
                res_start = candidate
                res_len = mid
                l = mid + 1  # try longer
            else:
                r = mid - 1  # try shorter

        return s[res_start:res_start + res_len]
