class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # O(n), O(n)

        pre = defaultdict(int)
        pre[0] = 1

        curr = res = 0

        for i in range(len(nums)):

            curr += nums[i]
            diff = curr - k

            if diff in pre:
                res += pre[diff]

            pre[curr] += 1
        
        return res
            