class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        # O(n), O(n) similar to LC 560
        
        pre = defaultdict(int)
        pre[0] = 1

        curr = res = 0

        for n in nums:

            curr = curr + n
            diff = curr % k

            if diff in pre:
                res += pre[diff]
            
            pre[diff] += 1
        
        return res