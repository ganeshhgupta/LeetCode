class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, num in enumerate(nums) if num == key]
        result = set()

        for j in key_indices:
            start = max(0, j - k)
            end = min(len(nums), j + k + 1)
            for i in range(start, end):
                result.add(i)

        return sorted(result)
