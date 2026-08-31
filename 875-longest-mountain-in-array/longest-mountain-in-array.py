class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        # O(n^2), O(1)
        res = 0

        for i in range(1, len(arr) - 1):

            if arr[i - 1] >= arr[i] or arr[i] <= arr[i + 1]: # i must be a peak
                continue

            l, r = i, i

            while l > 0 and arr[l - 1] < arr[l]: # Expand left: must be increasing toward peak
                l -= 1

            while r < len(arr) - 1 and arr[r] > arr[r + 1]: # Expand right: must be decreasing from peak
                r += 1

            res = max(res, r - l + 1)

        return res