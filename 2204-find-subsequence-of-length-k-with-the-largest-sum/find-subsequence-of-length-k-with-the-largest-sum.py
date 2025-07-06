class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        indexed_nums = list(enumerate(nums))
        top_k = heapq.nlargest(k, indexed_nums, key=lambda x: x[1])
        top_k.sort(key=lambda x: x[0])
        return [val for idx, val in top_k]