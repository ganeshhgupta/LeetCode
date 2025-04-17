class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = defaultdict(list)

        for i in range(len(nums)):
            pairs[nums[i]].append(i)

        count = 0
        for indices in pairs.values():
            n = len(indices)
            for i in range(n):
                for j in range(i + 1, n):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
        return count
