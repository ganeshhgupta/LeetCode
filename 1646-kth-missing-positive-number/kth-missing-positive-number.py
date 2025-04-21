class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev = 0
        for i in range(len(arr)):
            gap = arr[i] - prev - 1
            if k <= gap:
                return prev + k
            k -= gap
            prev = arr[i]
        return arr[-1] + k
