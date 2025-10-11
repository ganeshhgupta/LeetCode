class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # O(n), O(n)

        n = len(nums)
        k %= n  # handle k > n
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
